from fastapi import FastAPI, Depends
from api.generate_tree import router as generate_tree_router
from services.decision_tree import process_all_pdfs_concurrently
from cache import get_cache

app = FastAPI()

cache = get_cache()

@app.on_event("startup")
async def startup_event():
    directory_path = "./policies"
    cache["policies"] = await process_all_pdfs_concurrently(directory_path)
    print("Cache initialized")

app.include_router(generate_tree_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
