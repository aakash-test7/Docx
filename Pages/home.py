import streamlit as st

def home_page():
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
    
    # Main title
    st.markdown('<h1 class="center-title" style="font-size: 6rem;">TECHWILL x DOCX</h1>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    
    col1, col2 = st.columns(2)
    
    # Summary Engine Card
    with col1.container(border=True, key="doc11"):
        st.markdown('<h2 class="center-heading">PDF Summarizer</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **Gemini-Powered** • Utilizes Google Gemini API for deep contextual understanding  
        - **Instant Summaries** • Converts long documents into digestible insights  
        - **Highlights & Takeaways** • Captures key points, stats, and sections  
        - **Smart Compression** • Preserves meaning while reducing clutter  
        - **GCP Hosted** • Scalable, fast, and reliable  
        """)

    # FAQ & Insights Card
    with col2.container(border=True, key="doc12"):
        st.markdown('<h2 class="center-heading">FAQ & Deep Insights</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **Conversational Q&A** • Ask custom questions, get direct answers  
        - **Reference Links** • Shows which parts of the document support the answers  
        - **Deep Reasoning** • Handles context-heavy or technical queries  
        - **Gemini Integration** • Handles logic, nuance, and domain-specific text  
        - **Live Testing** • Query documents right in your browser  
        """)

    # Key Features
    with st.container(border=True, key="doc2"):
        st.markdown('<h2 class="center-heading">Key Features</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **Secure Auth** • Implements robust user authentication and authorization to ensure that document access and insights are restricted to authorized individuals only. Supports integration with Firebase for easy scalability and multi-user access control.  
        - **Reference-Based Answers** • Every response is grounded in the actual content of the uploaded PDF. No fabricated data—just accurate, referenced answers that link back to specific parts of the document.  
        - **User-Friendly UI** • Built entirely with Streamlit, the interface is clean, intuitive, and responsive. Whether you're a researcher, student, or professional, you'll find it easy to navigate and interact with.  
        - **Cloud Ready** • The application is deployed on Google Cloud Platform (GCP), ensuring high availability, secure data handling, and seamless scaling for large volumes of documents and users.  
        - **Insight Engine** • Transforms lengthy and complex documents into actionable knowledge. It identifies summaries, FAQs, highlights, and even deep analytical answers using Gemini API.  
        - **Flexible Input** • Compatible with a wide range of PDF types—research papers, legal contracts, corporate reports, academic books, and technical manuals—making it ideal for diverse professional and academic use cases.  
        """)
    
    # Technical Stack
    col1, col2 = st.columns(2)
    with col1.container(border=True, key="doc31"):
        st.markdown('<h2 class="center-heading">Tech Stack</h2>', unsafe_allow_html=True)
        st.markdown("""
        - Python 
        - Streamlit
        - Google Cloud Platform
        - PDFPlumber 
        - Railway  
        """)

    with col2.container(border=True, key="doc32"):
        st.markdown('<h2 class="center-heading">Use Cases</h2>', unsafe_allow_html=True)
        st.markdown("""
        - Research Paper Review  
        - Business Contract Summarization  
        - Product Manuals  
        - Legal Documents & Policy Digests  
        - Educational Material Breakdown  
        """)

    # Footer
    st.markdown("""
    <div class="footer">
        © Aakash Kharb
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""<style>
        .center-title {
            text-align: center;
            margin-top: 0;
        }
        .center-heading {
            text-align: center;
        }
        .footer {
            background-color: #fff;
            color: #000;
            text-align: center;
            padding: 1rem 0;
            margin-top: 3rem;
            border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""<style>.stVerticalBlock.st-key-doc11 {background-color: #6c7b7b; color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-doc11:hover {background-color: rgba(245,245,245,0.8); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    st.markdown("""<style>.stVerticalBlock.st-key-doc12 {background-color: #6c7b7b; color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-doc12:hover {background-color: rgba(245,245,245,0.8); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    st.markdown("""<style>.stVerticalBlock.st-key-doc2 {background-color: #6c7b7b; color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-doc2:hover {background-color: rgba(245,245,245,0.8); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    st.markdown("""<style>.stVerticalBlock.st-key-doc31 {background-color: #6c7b7b; color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-doc31:hover {background-color: rgba(245,245,245,0.8); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    st.markdown("""<style>.stVerticalBlock.st-key-doc32 {background-color: #6c7b7b; color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-doc32:hover {background-color: rgba(245,245,245,0.8); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
if __name__ == "__main__":
    home_page()