from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Serve the index.html file
@app.get("/")
async def serve_index():
    file_path = "./index.html"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="index.html not found")
    return FileResponse(file_path)

# Chat endpoint
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    if not user_input:
        raise HTTPException(status_code=400, detail="No input provided")

    try:
        # Updated API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        message = response['choices'][0]['message']['content']
        return JSONResponse(content={"reply": message})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
