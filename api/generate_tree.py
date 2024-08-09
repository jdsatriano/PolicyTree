from fastapi import APIRouter
from cache import get_cache
from services.decision_tree import process_all_pdfs_concurrently
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/generate-decision-trees/")
async def generate_decision_trees():
    cache = get_cache()
    print(cache)
    if "policies" in cache and cache["policies"]:
        return JSONResponse(content={"policies": cache["policies"]})
    else:
        directory_path = "./policies"
        cache["policies"] = await process_all_pdfs_concurrently(directory_path)
        return JSONResponse(content={"policies": cache["policies"]})
