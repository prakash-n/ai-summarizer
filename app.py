import streamlit as st
import tempfile

from main import summarize_text
from ingest.pdf_loader import load_pdf
from ingest.ocr_loader import ocr_pdf


# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Summarizer", layout="wide")


# --- HEADER ---
st.title("📄 AI Document Summarizer")
st.markdown("Summarize text or PDFs using local AI (Ollama)")

st.divider()


# --- INPUT SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    input_type = st.radio("Choose Input Type", ["Text", "PDF"])

with col2:
    mode = st.selectbox(
        "Summary Mode",
        ["very short", "brief", "bullet", "detailed", "insights"]
    )


text = ""
uploaded_file = None


# --- TEXT INPUT ---
if input_type == "Text":
    text = st.text_area("Paste your text here", height=300)


# --- PDF INPUT ---
elif input_type == "PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])


st.divider()


# --- HELPER: SAVE TEMP FILE ---
def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        return tmp.name


# --- SUMMARIZE BUTTON ---
if st.button("🚀 Generate Summary"):

    # --- TEXT FLOW ---
    if input_type == "Text":

        if not text.strip():
            st.error("❌ Please enter some text")
        else:
            st.info(f"📄 Text length: {len(text)} characters")

            with st.spinner("Summarizing..."):
                result = summarize_text(text, mode)

            st.success("✅ Summary generated!")

            st.subheader("📌 Summary")
            st.markdown(result)

            st.download_button(
                "⬇️ Download Summary",
                result,
                file_name="summary.txt"
            )


    # --- PDF FLOW ---
    elif input_type == "PDF":

        if uploaded_file is None:
            st.error("❌ Please upload a PDF file")
        else:
            file_path = save_uploaded_file(uploaded_file)

            with st.spinner("📄 Processing PDF..."):

                try:
                    text = load_pdf(file_path)

                    if len(text.strip()) < 200:
                        st.warning("⚠️ Weak text detected → using OCR...")
                        text = ocr_pdf(file_path)

                except Exception:
                    st.warning("⚠️ Standard read failed → using OCR...")
                    text = ocr_pdf(file_path)

            st.info(f"📄 Extracted text length: {len(text)} characters")

            # Optional preview
            with st.expander("🔍 Preview extracted text"):
                st.write(text[:500])

            with st.spinner("🧠 Generating summary..."):
                result = summarize_text(text, mode)

            st.success("✅ Summary generated!")

            st.subheader("📌 Summary")
            st.markdown(result)

            st.download_button(
                "⬇️ Download Summary",
                result,
                file_name="summary.txt"
            )