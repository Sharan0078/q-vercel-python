from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
import json

app = FastAPI()

# Enable CORS for all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data once
with open("q-vercel-python.json") as f:
    data = json.load(f)

# API endpoint
@app.get("/api")
def get_marks(name: List[str]):
    name_to_marks = {entry["name"]: entry["marks"] for entry in data}
    marks = [name_to_marks.get(n, None) for n in name]
    return JSONResponse(content={"marks": marks})
