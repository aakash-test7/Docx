import streamlit as st
from backend import generate_signed_url

def tutorial_page():
    st.title("Tutorials Page")
    st.write("**Learn how to use this interface**")

    video_url = generate_signed_url("Video/video1.mp4")
    if video_url:
        st.video(video_url, start_time=0)
    else:
        st.warning("Could not generate streaming URL")

if __name__ == "__main__":
    tutorial_page()
