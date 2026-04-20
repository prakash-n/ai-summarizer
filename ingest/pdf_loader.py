from pypdf import PdfReader

def load_pdf(file_path):
    try:
        reader = PdfReader(file_path)
    except Exception:
        raise ValueError("Could not read PDF (corrupted or unsupported)")

    text = ""
    valid_pages = 0

    for i, page in enumerate(reader.pages):
        try:
            content = page.extract_text()
            
            if content and len(content.strip()) > 50:  # filter weak pages
                text += content + "\n"
                valid_pages += 1

        except Exception:
            continue  # skip broken pages

    if valid_pages == 0:
        raise ValueError("No usable text found (likely scanned PDF)")

    print(f"✅ Extracted text from {valid_pages} pages")

    return text