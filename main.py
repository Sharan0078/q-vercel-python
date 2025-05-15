from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
from fastapi.responses import JSONResponse
from fastapi.requests import Request

app = FastAPI()

# CORS enabled
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)
    marks_dict = {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(name: List[str]):
    result = [marks_dict.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
