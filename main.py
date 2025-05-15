from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins (you can restrict this later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")  # Ensure GET route exists
async def read_data():
    return {"message": "Hello, world!"}
