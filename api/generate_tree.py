from fastapi import APIRouter
from services.decision_tree import process_all_pdfs_concurrently
from fastapi.responses import JSONResponse

router = APIRouter()
cache = {}

@router.get("/generate-decision-trees/")
async def generate_decision_trees():
    if "policies" in cache and cache["policies"]:
        return JSONResponse(content={"policies": cache["policies"]})
    else:
        directory_path = "./policies"
        cache["policies"] = await process_all_pdfs_concurrently(directory_path)
        return JSONResponse(content={"policies": cache["policies"]})
