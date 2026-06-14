from fastapi import APIRouter, UploadFile, File
from services.resume_parser import extract_resume_text
from services.resume_parser import extract_section
from services.resume_analyzer import (
    analyze_resume
)

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    text = extract_resume_text(pdf_bytes)
    analysis = analyze_resume(text)
    return {
    "analysis": analysis
}