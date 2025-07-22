from .cppbind import AddDelFiles as AD
from langchain_core.tools import Tool
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import MarkdownTextSplitter
import os
from dotenv import load_dotenv
import requests
from typing import Iterable,Optional,Any
load_dotenv()

class StandVectorStore:
    def __init__(self, name:str="stand"):
        self.embedding_model = DashScopeEmbeddings(
            model="text-embedding-v3"
        )
        self.vec_store=Chroma(name, self.embedding_model)
        self.retriever =self.vec_store.as_retriever(search_type="mmr",search_kwargs={"k":10})
        self.retriever_tool = Tool(
            name="retriever_tool",
            func=self._retriever_tool_func,
            description="This tool searches and returns the information of math data."
        )

    
    def add_texts(self,texts: Iterable[str],metadatas: Optional[list[dict]] = None,*,ids: Optional[list[str]] = None,**kwargs: Any):
        """
        添加文本到向量存储中，不会写入本地文件系统
        """
        self.vec_store.add_texts(texts,metadatas,ids,**kwargs)

    
    def _retriever_tool_func(self, quary: str) -> str:
        """
        This tool searches and returns the information of math data.
        """
        docs = self.retriever.invoke(quary)
        if not docs:
            return "I found no relevant information in the MathData"
        results = []
        for i, doc in enumerate(docs):
            results.append(f"Document {i+1} :\n {doc.page_content}")
        return "\n\n".join(results)

class VectorStore(StandVectorStore):
    def __init__(self , md_dir:str,store_dir:str,name:str="mathdata"):
        """
        初始化向量存储类
        """
        super().__init__()
        self.md_dir = md_dir
        self.store_dir = store_dir
        self.vec_store=Chroma(name,self.embedding_model,store_dir)
        self.sync_store()
    
    def sync_store(self):
        """
        同步向量存储
        """
        all_metadata = self.vec_store.get(include=["metadatas"])
        metadata_docs=all_metadata["metadatas"]
        adds,dels=AD.add_del_files(metadata_docs, self.md_dir)
        if adds:
            loader = DirectoryLoader(
                self.md_dir,
                glob=list(adds),
                loader_cls=UnstructuredMarkdownLoader, 
                use_multithreading=True
            )
            doc_pages = loader.load()
            text_spliter = MarkdownTextSplitter(chunk_size=150, chunk_overlap=20)
            doc_chunk = text_spliter.split_documents(doc_pages)
            self.vec_store.add_documents(doc_chunk)
            print(f"vec_store 已添加: {adds}\n")
        if dels:
            matching_ids = [
            current_id
            for current_id, current_meta in zip(all_metadata['ids'], all_metadata['metadatas'])
                if os.path.basename(current_meta["source"]) in dels]
            self.vec_store.delete(ids=matching_ids)
            print(f"vec_store 已删除: {dels}\n")
        print("sync_store 完成")
    
    def post_pdf(self,pdf_dir:str):
        if "MINERU_API_KEY" not in os.environ:
            os.environ["MINERU_API_KEY"] = input("Enter your MINERU API key: ")

        url='https://mineru.net/api/v4/file-urls/batch'
        
        header = {
        'Content-Type':'application/json',
        'Authorization':os.environ["MINERU_API_KEY"]}
        data = {
        "enable_formula": True,
        "language": "auto",
        "enable_table": True,
        "model_version":"v2",
            "files": [
                {"name":self.add_files_names[i], "is_ocr": True }
                for i in range(len(self.add_files_names))
            ]}
        file_path = [os.path.join(pdf_dir,file)+".pdf" for file in self.add_files_names]
        
        try:
            response = requests.post(url,headers=header,json=data)
            if response.status_code == 200:
                result = response.json()
                print('request success.' )
                if result["code"] == 0:
                    batch_id = result["data"]["batch_id"]
                    self.batch_id = batch_id
                    urls = result["data"]["file_urls"]
                    for i in range(0, len(urls)):
                        with open(file_path[i], 'rb') as f:
                            res_upload = requests.put(urls[i], data=f)
                            if res_upload.status_code == 200:
                                print("upload success")
                            else:
                                print("upload failed")
                else:
                    print('apply upload url failed,reason:{}'.format(result.msg))
            else:
                print('response not success. status:{} ,result:{}'.format(response.status_code, response))
        except Exception as err:
            print(err)

    def get_pdf_url(self,maxWaitingTime:int=20):
        import time
        url = f'https://mineru.net/api/v4/extract-results/batch/'+self.batch_id
        header = {
            'Content-Type':'application/json',
            'Authorization':os.environ["MINERU_API_KEY"]
        }
        res = requests.get(url, headers=header)
        count=1
        maxWaitingTime=maxWaitingTime*2
        if res.status_code == 200:
            for i in range(maxWaitingTime):
                res = requests.get(url, headers=header)
                state=[item["state"] for item in res.json()["data"]["extract_result"]]
                time.sleep(30)
                print(f"waiting for {count/2} minutes")
                count+=1
                if isinstance(state,list) and all(item=="done" for item in state):
                    self.zip_urls=[item["full_zip_url"] for item in res.json()["data"]["extract_result"]]
                    print(self.zip_urls)
                    break
            if count>maxWaitingTime:
                raise TimeoutError("waiting for too long, please check the batch_id")

        else:
            print(res.status_code)
            print(res.json())

    def download_zip(self):
        #self.zip_urls self.add_files_names
        from urllib.request import urlretrieve

        save_dirs = [f"./temp/{filename}" for filename in self.add_files_names]
        self.save_dirs=save_dirs
        download_paths=[os.path.join(save_dir,filename+".zip") for save_dir,filename in zip(save_dirs,self.add_files_names)]
        self.download_paths=download_paths
        [os.makedirs(save_dir, exist_ok=True) for save_dir in save_dirs]
        try:
            for url, save_path in zip(self.zip_urls, download_paths):
                urlretrieve(url, save_path)
                print(f"文件已成功下载到：{save_path}")
        except Exception as e:
            print(f"下载失败：{e}")

    def unzip_files(self):
        """解压文件"""
        import zipfile
        # 待解压的 ZIP 文件路径
        print(self.download_paths)
        for file_zip,save_dir in zip(self.download_paths,self.save_dirs):
            with zipfile.ZipFile(file_zip, 'r') as zip_ref:
                zip_ref.extractall(save_dir)

    def move_delete_files(self):
        """将解压后的文件移动到md_dir中，并且删除源temp文件夹"""
        import shutil
        # 配置参数 - 请根据需要修改
        source_dirs = self.save_dirs
        target_dir = self.md_dir
        old_file_name = "full.md"
        new_file_names = [name + ".md" for name in self.add_files_names] 

        try:
            # 构建文件路径
            source_files = [os.path.join(source_dir, old_file_name) for source_dir in source_dirs]
            target_files = [os.path.join(target_dir, name ) for name in new_file_names]
            
            
            # 创建目标文件夹
            os.makedirs(target_dir, exist_ok=True)
            
            # 移动文件(自动处理重命名)
            for source_file,target_file in zip(source_files,target_files):
                shutil.move(source_file, target_file)
                print(f"成功: 文件已移动到 {target_file}")
            

            shutil.rmtree("./temp")  # 递归删除非空文件夹
            print(f"已成功删除文件夹及内容: ./temp")
                
        except Exception as e:
            print(f"错误: {e}")

    def sync_md(self,pdf_dir:str,maxWaitingTime:int=10):
        pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
        
        pdf_file_names=[os.path.splitext(name)[0] for name in pdf_files]
        md_files=[f for f in os.listdir(self.md_dir) if f.lower().endswith('.md')]
        md_files_names=[os.path.splitext(name)[0] for name in md_files]
        add_files_names=list(set(pdf_file_names)-set(md_files_names))
        self.add_files_names=add_files_names
        if not add_files_names:
            print("no new pdf files to add")
            return
        self.post_pdf(pdf_dir)
        self.get_pdf_url(maxWaitingTime)
        self.download_zip()
        self.unzip_files()
        self.move_delete_files()
        self.sync_store()