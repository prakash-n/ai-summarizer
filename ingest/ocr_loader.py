from pdf2image import convert_from_path
import pytesseract


def ocr_pdf(file_path):
    try:
        images = convert_from_path(file_path)
    except Exception:
        raise ValueError("Failed to convert PDF to images for OCR")

    text = ""
    pages_processed = 0

    for i, image in enumerate(images):
        try:
            page_text = pytesseract.image_to_string(image)

            if page_text.strip():
                text += page_text + "\n"
                pages_processed += 1

        except Exception:
            continue

    if pages_processed == 0:
        raise ValueError("OCR failed to extract any text")

    print(f"🔍 OCR extracted text from {pages_processed} pages")

    return text