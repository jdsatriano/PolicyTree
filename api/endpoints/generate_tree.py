from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from services.decision_tree import generate_and_rank_tree
from services.text_extraction import extract_text_from_policy

router = APIRouter()

@router.post("/generate-decision-tree/")
async def generate_decision_tree(file: UploadFile = File(...)):
    try:
        text = extract_text_from_policy(file.file)
        criteria = generate_and_rank_tree(text)
        return JSONResponse(content=criteria)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
