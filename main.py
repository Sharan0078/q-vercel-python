from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins and GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the JSON data once at startup
with open("q-vercel-python.json") as f:
    students = json.load(f)

# Create a lookup dictionary for fast access
marks_dict = {student["name"]: student["marks"] for student in students}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    # For each name in query parameter, get the marks or None if not found
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}
