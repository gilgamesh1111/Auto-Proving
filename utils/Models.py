from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from typing import Annotated
load_dotenv()


import asyncio

class Prover:
    def __init__(self,model_ls: Annotated[list[str], "modelNames"]):
        self.model_ls=model_ls
        self.models_dict = {f"{model}_{i}":self.chatModel(model) for i, model in enumerate(self.model_ls)}

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
    
    async def ainvoke(self, *args, **kwargs):
        tasks = [model.ainvoke(*args, **kwargs) for model in self.models_dict.values()]
        results = await asyncio.gather(*tasks)
        
        return dict(zip(self.models_dict.keys(), results))
    
    
if __name__ == "__main__":
    import asyncio
    model_ls = ["AI-MO/Kimina-Prover-Preview-Distill-7B"]
    prover = Prover(model_ls)
    responses = asyncio.run(prover.ainvoke(r"use lean to prove 2 is not in \mathbb{Q}"))
    print(responses)
    print()
