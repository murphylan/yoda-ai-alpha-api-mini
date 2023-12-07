import os
from fastapi import APIRouter
from typing import List, Dict, Any
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient, errors
from pydantic import BaseModel
from .text import TextPrompt

# fastapi router
router = APIRouter()

# connect to mongo
client = MongoClient(os.getenv("MongoURI"))

# check the loaded env vars
all_values = dotenv_values(".env")
# print(all_values)


class Prompt(BaseModel):
    prompt: str


@router.post("/text/prompt")
def prompt(prompt: Prompt):
    
    # get prompt answer
    prompt_reply = TextPrompt.generate(prompt=prompt.prompt)

    return {
        "reply": prompt_reply,
        "prompt": prompt,
    }


