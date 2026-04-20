from chunking.chunker import chunk_text
from summarize.ollama_client import generate_summary
from postprocess.combiner import combine_summaries
from ingest.pdf_loader import load_pdf
from ingest.ocr_loader import ocr_pdf


def summarize_text(text, mode):
    chunks = chunk_text(text)
    partials = []

    for i, chunk in enumerate(chunks):
        summary = generate_summary(chunk, mode)

        print(f"🧩 Chunk {i+1} summary:", "OK" if summary else "FAILED")

        if summary:
            partials.append(summary)

    if not partials:
        raise ValueError("No summaries generated")

    final = combine_summaries(partials)
    return final


if __name__ == "__main__":
    try:
        choice = input("Choose input type (1 = text, 2 = pdf): ")

        # --- TEXT INPUT ---
        if choice == "1":
            text = input("Paste your text:\n")
            print(f"📄 Text length: {len(text)} characters")

        # --- PDF INPUT ---
        elif choice == "2":
            file_path = input("Enter PDF file path: ")
            print(f"📁 Loading PDF from: {file_path}")

            try:
                text = load_pdf(file_path)

                # if extracted text is too small -> switch to OCR
                if len(text.strip()) < 200:
                    print("⚠️ Weak text detected, switching to OCR...")
                    text = ocr_pdf(file_path)

            except Exception:
                print("⚠️ Standard PDF read failed, attempting OCR...")
                try:
                    text = ocr_pdf(file_path)
                except Exception:
                    raise ValueError("Both standard PDF extraction and OCR failed")

            print(f"📄 Text length: {len(text)} characters")
            print("📝 Preview:", text[:200])

        else:
            print("Invalid choice")
            exit()

        # --- MODE SELECTION ---
        mode = input("Choose summary mode (very short / brief / bullet / detailed / insights): ")

        # --- RUN SUMMARIZATION ---
        result = summarize_text(text, mode)

        print("\nFINAL SUMMARY:\n")
        print(result)

    except Exception as e:
        print("\n❌ Error:", str(e))

        msg = str(e).lower()

        if "pdf" in msg:
            print("👉 Tip: File may be corrupted or scanned (image-based PDF)")

        elif "extractable" in msg:
            print("👉 Tip: This looks like a scanned PDF. OCR is needed.")

        elif "summaries" in msg:
            print("👉 Tip: Model failed to generate output. Try a different mode or input.")

        else:
            print("👉 Tip: Check if Ollama is running (ollama serve)")