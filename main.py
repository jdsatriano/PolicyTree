from fastapi import FastAPI, Depends
from api.generate_tree import router as generate_tree_router
from services.decision_tree import process_all_pdfs_concurrently

app = FastAPI()
app.include_router(generate_tree_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
