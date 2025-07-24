from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from typing import Annotated
load_dotenv()


class Prover:
    model_ls: Annotated[list[str], "modelNames"]

    def __init__(self):
        self.models = [self.chatModel(model) for model in self.model_ls]

    def chatModel(self, modelName: str):
        llm = HuggingFaceEndpoint(
            repo_id=modelName,
            task="text-generation",
            do_sample=False,
            repetition_penalty=1.0,
            provider="auto",  # let Hugging Face choose the best provider for you
            return_full_text=True,)
        chat_model = ChatHuggingFace(llm=llm)   
        return chat_model
    
    async def invoke(self, *args, **kwargs):
        return {f"{model}_{self.models.index(model)}": await model.ainvoke(*args, **kwargs) for model in self.models}
    
if __name__ == "__main__":
    import asyncio
    Prover.model_ls = ["AI-MO/Kimina-Prover-Preview-Distill-7B" for i in range(2)]
    prover = Prover()
    responses = asyncio.run(prover.invoke(r"use lean to prove 2 is not in \mathbb{Q}"))
    print(responses)
