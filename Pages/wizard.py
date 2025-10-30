import streamlit as st
import streamlit.components.v1 as components

def integrate_website_page():
    st.title("PDF Utility Wizard")

    st.markdown(
        """
        ## Integration of Mac PDF Wizard App

        Below is the embedded version of the [Mac PDF Wizard App](https://mac-pdf-wizard-app.lovable.app). 
        This tool can help you with PDF processing tasks like splitting, merging, and editing PDF documents.
        """
    )

    # Embed the external website in an iframe (using HTML)
    website_url = "https://mac-pdf-wizard-app.lovable.app"
    
    # HTML code to embed the website
    html_code = f"""
    <iframe src="{website_url}" width="100%" height="800px" frameborder="0">
        Your browser does not support iframes.
    </iframe>
    """

    # Display the iframe inside Streamlit
    components.html(html_code, height=850)

if __name__ == "__main__":
    integrate_website_page()
