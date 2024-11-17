import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv 

app = FastAPI() 
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chats/")
async def chat(request: ChatRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are the best assistant."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=1000
        )
        reply = response["choices"][0]["message"]["content"]
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


        