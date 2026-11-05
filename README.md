# Generative AI Document Analyzer

An intelligent web application that uses **Prompt Engineering** and **Large Language Models (LLMs)** to analyze, summarize, and extract actionable insights from long-form documents.

## Key Features
- **Intelligent Summarization:** Automatically distills complex documents into executive summaries, bullet points, or structured tables.
- **Entity & Metric Extraction:** Detects key performance indicators (KPIs), numerical figures, and named entities.
- **REST API with FastAPI:** High-performance async backend exposing endpoints for document ingestion and Q&A.
- **Interactive UI with Streamlit:** User-friendly frontend allowing real-time document upload, prompt customization, and chat.

## Architecture
```
[ Document Input (PDF / TXT) ]
              │
              ▼
   [ Text Preprocessor & Chunker ]
              │
              ▼
[ Prompt Engineering Engine (Templates) ]
              │
              ▼
    [ LLM Processing Module ]
              │
              ▼
[ Structured Output & Interactive Chat UI ]
```

## Installation & Setup
```bash
git clone https://github.com/syedhammad1014/Generative-AI-Document-Analyzer.git
cd Generative-AI-Document-Analyzer
pip install -r requirements.txt
```

### Running the FastAPI Backend
```bash
python main.py
```
Open documentation at `http://localhost:8000/docs`.

### Running the Streamlit Interface
```bash
streamlit run app.py
```

## Technologies
- **Python 3.10+**
- **FastAPI & Uvicorn**
- **Streamlit**
- **Prompt Engineering & LLM APIs**
