import streamlit as st
import inspect
from Pages.logic import extract_text, chunk_text, process_with_gemini

def src_code_page():
    st.title("Source Code")
    st.markdown("Below are the core logic functions used in this app:")

    with st.expander("📄 `extract_text()` - Extract text from PDF"):
        st.code(inspect.getsource(extract_text), language="python")

    with st.expander("📄 `chunk_text()` - Chunk extracted text"):
        st.code(inspect.getsource(chunk_text), language="python")

    with st.expander("📄 `process_with_gemini()` - Gemini API interaction"):
        st.code(inspect.getsource(process_with_gemini), language="python")

if __name__ == "__main__":
    src_code_page()
