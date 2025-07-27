from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import threading as thd
from queue import Queue
from typing import Annotated
from langchain_ollama import ChatOllama
load_dotenv()


import asyncio

class Prover:
    def __init__(self,model_ls: Annotated[list[str], "modelNames"],plantform: str = "huggingface"):
        self.model_ls=model_ls
        if plantform == "huggingface":
            self.models_dict = {f"{model}_{i}":self.chatModel(model) for i, model in enumerate(self.model_ls)}
        elif plantform == "local":
            self.models_dict = {f"{model}_{i}":self.chatLocalModel(model) for i, model in enumerate(self.model_ls)}

    def chatLocalModel(self, modelName: str):
        llm = ChatOllama(
            model=modelName,
            temperature=0.0,)
        return llm
            
    def chatModel(self, modelName: str):
        llm = HuggingFaceEndpoint(
            repo_id=modelName,
            task="text-generation",
            do_sample=False,
            repetition_penalty=1.0,
            provider="auto",
            return_full_text=True,
        )
        chat_model = ChatHuggingFace(llm=llm)   
        return chat_model
    
    def ainvoke(self, *args, **kwargs) :
        """
        使用多线程同时调用所有模型。
        """
        results_queue = Queue()

        def worker(key, model):
            result = model.invoke(*args, **kwargs)
            results_queue.put((key, result))

        threads = []
        for key, model in self.models_dict.items():
            thread = thd.Thread(target=worker, args=(key, model))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        final_results = {}
        while not results_queue.empty():
            key, result = results_queue.get()
            final_results[key] = result
            
        return final_results
    
if __name__ == "__main__":
    model_ls = ["hf.co/DevQuasar/AI-MO.Kimina-Prover-Preview-Distill-7B-GGUF:Q4_K_M"]
    prover = Prover(model_ls,"local")
    responses = prover.ainvoke(r"use lean to prove 2 is not in \mathbb{Q}")
    print(responses)
