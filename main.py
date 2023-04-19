# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from langchain.vectorstores import FAISS
from langchain import OpenAI
from langchain.chains import RetrievalQA 
from langchain.embeddings import HuggingFaceEmbeddings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
name = FAISS.load_local(embeddings=HuggingFaceEmbeddings(),folder_path='')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(message: Message):
    user_message = message.message
    reply = process_message(user_message)
    return {"reply": reply}

def process_message(user_message: str) -> str:
    qa = RetrievalQA.from_chain_type(llm=OpenAI(model='text-davinci-003',openai_api_key="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"), chain_type='stuff', retriever=name.as_retriever())
    ans = qa.run(user_message)
    return f"Bot {ans}"
