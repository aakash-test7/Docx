import streamlit as st
import pdfplumber
import google.generativeai as genai
import tempfile
import os
from Pages.security_login import insert_pdf_record

# Constants
CHUNK_SIZE = 2000
GEMINI_API_KEY = st.secrets["gemini_api_key"]["GEMINI_API_KEY"]

def extract_text(pdf_file):
    """Extract text from PDF file using pdfplumber."""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return None
    return text.strip()

def chunk_text(text, chunk_size=CHUNK_SIZE):
    """Split text into chunks of specified size."""
    if not text:
        return []
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def translate_content(api_key, content, target_language):
    """Translate content to target_language preserving Markdown."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        prompt = f"Translate the following text to {target_language}, preserving Markdown formatting:\n\n{content}"
        response = model.generate_content(prompt)
        return response.text or content
    except Exception as e:
        st.error(f"Translation Error: {e}")
        return content

def process_with_gemini(api_key, chunks, question=None):
    """Process text chunks with Gemini API and return formatted results."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    except Exception as e:
        st.error(f"Failed to configure Gemini API: {e}")
        return None

    result = ""
    progress_bar = st.progress(0)
    
    if question:
        # Process user question against all chunks
        try:
            combined_text = "\n\n".join(chunks)
            response = model.generate_content(
                f"""Answer the following question based on the provided document content.
                Be precise and only use information from the document.
                If the answer isn't in the document, say "The document doesn't contain information about this."

                Question: {question}

                Document Content:
                {combined_text}
                """
            )
            return response.text if response.text else "No answer could be generated."
        except Exception as e:
            st.error(f"Gemini API Error: {e}")
            return None
    else:
        # Original processing for summary and FAQs
        for i, chunk in enumerate(chunks):
            try:
                response = model.generate_content(
                    f"""**Formatting Requirements:**
                    - Use **Markdown formatting** (headings, bold, bullet points, etc.) for clarity.
                    - Clearly separate each section with headings like `## Summary`, `## FAQs`, `## Highlights`, and `## References`.
                    - Ensure all content is easily scannable and user-friendly.
                    - Do not repeat content across chunks - each chunk should contain unique analysis.
                        
                    Please carefully analyze the following text and return a well-organized output with these structured sections:

                    1. **Summary**: Provide a concise and clear summary that captures the core ideas of this section.

                    2. **FAQs**: Create 3-5 relevant questions and answers from this section. Format as:
                    - **Q:** Question text
                    - **A:** Answer text

                    3. **Important Highlights**: List notable facts, figures, or insights from this section.

                    4. **References**: Include any references mentioned in this section.

                    Here is the content to analyze:
                    --------------------------
                    {chunk}
                    """
                )
                if response.text:
                    result += response.text + "\n\n"
                progress_bar.progress((i + 1) / len(chunks))
            except Exception as e:
                st.error(f"Gemini API Error on chunk {i+1}: {e}")
                continue
        
        progress_bar.empty()
        # merge chunks into one cohesive output
        merged = result.strip() if result else None
        if merged and len(chunks) > 1:
            try:
                merge_prompt = f"""Merge the following analyses into one cohesive output, preserving Markdown formatting:\n\n{merged}"""
                merged_resp = model.generate_content(merge_prompt)
                return merged_resp.text or merged
            except Exception as e:
                st.error(f"Gemini API Error during merge: {e}")
                return merged
        return merged

def pdf_page():
    """Main Streamlit application function."""
    con=st.container(border=True)
    with con:
        st.title("📄 PDF Summarizer & FAQ Generator")
        st.markdown("Upload a PDF to generate a comprehensive summary and FAQ section.")
        
        # Initialize session state
        if 'pdf_recorded' not in st.session_state:
            st.session_state.pdf_recorded = False
        if 'processed_result' not in st.session_state:
            st.session_state.processed_result = None
        if 'pdf_processed' not in st.session_state:
            st.session_state.pdf_processed = False
        if 'pdf_text' not in st.session_state:
            st.session_state.pdf_text = ""
        if 'chunks' not in st.session_state:
            st.session_state.chunks = []
        if 'pdf_filename' not in st.session_state:
            st.session_state.pdf_filename=None
        if 'language' not in st.session_state:
            st.session_state.language = "English"

        # Language selection dropdown
        languages = ["English", "Hindi", "French", "German", "Spanish"]
        st.session_state.language = st.selectbox(
            "Select Language", languages, index=languages.index(st.session_state.language)
        )

        # File uploader
        pdf_file = st.file_uploader(
            "Choose a PDF file",
            type=["pdf"],
            accept_multiple_files=False,
            help="Upload a PDF document to analyze"
        )
        if pdf_file is not None:
            if pdf_file.name != st.session_state.get("pdf_filename"):
                st.session_state.pdf_filename = pdf_file.name
                st.session_state.pdf_processed = False
                st.session_state.pdf_recorded = False

        if pdf_file is not None and not st.session_state.pdf_processed:
            col1,col2,col3=st.columns([1,2,1])
            if col2.button("🚀 Generate Summary & FAQ", type="primary",use_container_width=True):
                with st.spinner("Processing your PDF...",show_time=True):
                    # Create temporary file
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(pdf_file.read())
                        tmp_file_path = tmp_file.name
                    
                    try:
                        # Extract text
                        text = extract_text(tmp_file_path)
                        if not text:
                            st.error("No extractable text found in the PDF.")
                            return
                        
                        # Store in session state
                        st.session_state.pdf_text = text
                        st.session_state.chunks = chunk_text(text)
                        
                        # Get results from Gemini
                        result = process_with_gemini(GEMINI_API_KEY, st.session_state.chunks)
                        
                        if result:
                            # Translate summary if needed
                            if st.session_state.language != "English":
                                result = translate_content(GEMINI_API_KEY, result, st.session_state.language)
                            st.session_state.processed_result = result
                            st.session_state.pdf_processed = True
                            st.toast("Analysis completed successfully!")
                    finally:
                        # Clean up temporary file
                        try:
                            os.unlink(tmp_file_path)
                        except:
                            pass

        # Display results if available
        if st.session_state.processed_result:
            st.subheader("📃 Generated Summary and FAQ")
            st.markdown(st.session_state.processed_result, unsafe_allow_html=True)

            if not st.session_state.get("pdf_recorded", False):
                insert_pdf_record(st.session_state.pdf_filename)
                st.session_state.pdf_recorded = True

            col1,col2,col3=st.columns([1,2,1])
            col2.download_button(
                label="💾 Download Results",
                data=st.session_state.processed_result,
                file_name="document_summary_faq.md",
                mime="text/markdown",
                help="Download the generated summary and FAQ in Markdown format",
                on_click="ignore",
                use_container_width=True
            )

            # Question input section
            st.divider()
            st.subheader("❓ Ask a Question About the Document")
            user_question = st.text_area(
                "Enter your question about the document content:",
                placeholder="What is the main topic of this document?",
                height=100
            )
            col1,col2,col3=st.columns([1,2,1])
            if col2.button("🔍 Get Answer", type="secondary",use_container_width=True):
                if user_question.strip():
                    with st.spinner("Searching for answer...",show_time=True):
                        answer = process_with_gemini(
                            GEMINI_API_KEY,
                            st.session_state.chunks,
                            user_question
                        )
                        if answer:
                            # Translate answer if needed
                            if st.session_state.language != "English":
                                answer = translate_content(GEMINI_API_KEY, answer, st.session_state.language)
                            st.markdown("### Answer:")
                            st.markdown(answer)
                        else:
                            st.error("Could not generate an answer.")
                else:
                    st.warning("Please enter a question first.")

            # Clear button
            st.divider()
            col1,col2,col3=st.columns(3)
            if col2.button("🧹 Clear All", type="primary",use_container_width=True):
                st.session_state.processed_result = None
                st.session_state.pdf_processed = False
                st.session_state.pdf_text = ""
                st.session_state.chunks = []
                st.session_state.pdf_filename = None
                st.session_state.pdf_recorded = False
                st.rerun()

if __name__ == "__main__":
    pdf_page()
