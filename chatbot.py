import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv 



load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
