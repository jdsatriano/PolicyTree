from fastapi import APIRouter
from services.decision_tree import process_all_pdfs_concurrently
from fastapi.responses import JSONResponse

router = APIRouter()
cache = {}

@router.get("/generate-decision-trees/")
async def generate_decision_trees():
    if "decision_trees" in cache and cache["decision_trees"]:
        return JSONResponse(content={"decision_trees": cache["decision_trees"]})
    else:
        directory_path = "./policies"
        cache["decision_trees"] = await process_all_pdfs_concurrently(directory_path)
        return JSONResponse(content={"decision_trees": cache["decision_trees"]})
