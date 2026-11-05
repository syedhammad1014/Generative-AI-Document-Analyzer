import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from analyzer import DocumentAnalyzer

app = FastAPI(
    title="Generative AI Document Analyzer API",
    description="REST API for automated document analysis, summarization, and query answering using LLMs.",
    version="1.0.0"
)

analyzer = DocumentAnalyzer()

class QueryRequest(BaseModel):
    document_text: str
    question: str

@app.get("/")
def root():
    return {"status": "online", "service": "Generative AI Document Analyzer"}

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    try:
        content = (await file.read()).decode("utf-8", errors="ignore")
        summary = analyzer.generate_summary(content)
        key_points = analyzer.extract_key_points(content)
        return {
            "filename": file.filename,
            "word_count": len(content.split()),
            "summary": summary,
            "key_points": key_points
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
def answer_query(req: QueryRequest):
    answer = analyzer.answer_question(req.document_text, req.question)
    return {"question": req.question, "answer": answer}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
