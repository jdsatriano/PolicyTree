from fastapi import FastAPI
from api.endpoints import generate_tree
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(generate_tree.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
