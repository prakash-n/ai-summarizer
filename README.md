
# 📄 AI Document Summarizer

A local AI-powered document summarizer using Ollama, with support for PDFs, OCR, and multiple summary modes.

---

## 🚀 Features

- Text and PDF input
- OCR fallback for scanned PDFs
- Multiple summary modes:
  - very short
  - brief
  - bullet
  - detailed
  - insights
- Streamlit web UI

---

## ▶️ Run Locally

- pip install -r requirements.txt
- ollama serve
- streamlit run app.py

## 📂 Project Structure

    ```bash

    ai-summarizer/
    ├── app.py              # Streamlit UI
    ├── main.py             # CLI entry point
    ├── config.py
    ├── ingest/             # PDF + OCR handling
    ├── summarize/          # LLM interaction
    ├── chunking/           # Text splitting
    ├── postprocess/        # Combine summaries
    ├── utils/              # Helper functions
    ├── docs/               # Notes / documentation
    └── requirements.txt
## 🚀 Future Improvements

- Chat with PDF (interactive Q&A)
- Improve summary quality with better prompts
- Add support for more file formats (DOCX, images)
- Deploy as a web application

## 🛠️ Tech Stack
- Python
- Ollama (local LLM)
- Streamlit
- Tesseract OCR

---
