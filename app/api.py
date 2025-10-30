from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List
import tempfile
import shutil
import os

from app.file_processing.file_reading import read_pdf_text
from app.text_translation.markdown_translate import markdown_translate

app = FastAPI(title="Article Translator API", version="0.1.0")


@app.get("/")
async def root():
    return {"status": "ok", "message": "Article Translator API"}


@app.post("/ocr")
async def process_file(file: UploadFile = File(...), lang: str = Form("en")):
    """Accept an uploaded image/PDF and return OCR'd lines.

    - file: uploaded file (image or PDF)
    - lang: language code for the OCR engine (default: "en")
    """
    tmp_path = None
    try:
        # save uploaded file to a temporary file
        suffix = os.path.splitext(file.filename or "")[1] or None
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # call the existing OCR helper (returns list of lines)
        text: str = read_pdf_text(tmp_path)

        translated_text = markdown_translate(text, "fr")
        with open("output_translated.md", "w", encoding="utf-8") as f:
            f.write(translated_text)
        return {"text": translated_text}

    except Exception as exc:
        print(f"Error processing file: {exc}")
        raise HTTPException(status_code=500, detail=str(exc))

    finally:
        try:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass
