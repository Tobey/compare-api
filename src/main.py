import os

from fastapi import FastAPI, UploadFile, File, Form, HTTPException

import conf
from pdf_service import PdfService
from utils import load_database, compare_data

app = FastAPI()
pdf_service = PdfService(key=conf.PDF_SERVICE_KEY)
database = load_database()


@app.post("/")
async def read_root(file: UploadFile = File(...), company_name: str = Form(...)):
    if company_name not in database.index:
        raise HTTPException(status_code=404, detail="Company not found in database")

    data  = await file.read()
    if len(data) == 0:
        raise HTTPException(status_code=400, detail="this file is empty")

    file_path = os.path.join("assets", file.filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="upload files from assets dir only")

    company_data = database.loc[company_name].to_dict()
    try:
        extracted_data = pdf_service.extract(file_path=file_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="file not found")

    comparison = compare_data(extracted_data, company_data)
    return comparison
