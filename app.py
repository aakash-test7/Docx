import streamlit as st
st.set_page_config("TechWill x Docx", layout="wide")
import Pages as pg
from Pages.security_login import update_visitor_count

st.logo("logo.gif")
st.markdown("""<style>.stLogo {    width: 48px;    height: 48px;}</style>""", unsafe_allow_html=True)

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
if 'first_access' not in st.session_state:
    st.session_state.first_access = True
if 'display_count' not in st.session_state:
    st.session_state.display_count = True
if "total_pdf" not in st.session_state:
    st.session_state.total_pdf=0
if "total_visitor" not in st.session_state:
    st.session_state.total_visitor=0

if st.session_state.first_access:
    st.session_state.total_visitor, st.session_state.total_pdf = update_visitor_count()

if st.session_state.display_count:
    st.toast(f"Visitor Count : {st.session_state.total_visitor}")
    st.session_state.display_count = False

with st.sidebar:
    col1,col2=st.columns(2)
    visitor_holder=col1.empty()
    pdf_holder=col2.empty()
    visitor_holder.metric(value=st.session_state.total_visitor,label="Visitors",delta=None,border=True)
    pdf_holder.metric(value=st.session_state.total_pdf,label="PDFs",delta=None,border=True)

if st.sidebar.button("Refresh⠀⠀⠀⠀",use_container_width=True,icon=":material/sync:"):
    st.session_state.total_visitor, st.session_state.total_pdf = update_visitor_count()
    visitor_holder.metric(value=st.session_state.total_visitor,label="Visitors",delta=None,border=True)
    pdf_holder.metric(value=st.session_state.total_pdf,label="PDFs",delta=None,border=True)
    st.rerun()

if st.sidebar.button("Home⠀⠀⠀⠀⠀",use_container_width=True,icon=":material/home:"):
    st.session_state.current_page = "Home"
if st.sidebar.button("Logic⠀⠀⠀⠀⠀",use_container_width=True,icon=":material/picture_as_pdf:"):
    st.session_state.current_page = "Logic"
if st.sidebar.button("Wizard⠀⠀⠀⠀",use_container_width=True,icon=":material/wand_stars:"):
    st.session_state.current_page = "Wizard"
if st.sidebar.button("Tutorial⠀⠀⠀⠀",use_container_width=True,icon=":material/movie:"):
    st.session_state.current_page = "Tutorials"
if st.sidebar.button("Source Code⠀",use_container_width=True,icon=":material/code:"):
    st.session_state.current_page = "Source Code"

st.sidebar.divider()

def open_link(url):
    st.components.v1.html(f'<script>window.open("{url}", "_blank");</script>', height=0)

if "social" not in st.session_state:
    st.session_state.social = False

if st.sidebar.button("Socials", use_container_width=True, icon=":material/person:"):
    st.session_state.social = not st.session_state.social

if st.session_state.social:
    if st.sidebar.button("Github", key="1button1", use_container_width=True):
        open_link("https://github.com/aakash-test7/")
    if st.sidebar.button("Youtube", key="1button2", use_container_width=True):
        open_link("https://youtube.com/@aakash5069")
    if st.sidebar.button("Linkedin", key="1button3", use_container_width=True):
        open_link("https://linkedin.com/in/aakash-kharb")
    if st.sidebar.button("X / Twitter", key="1button4", use_container_width=True):
        open_link("https://x.com/aakash_kharb")

# Function mapping for each page
functions = {
    "Home": pg.home_page,
    "Logic": pg.pdf_page,
    "Wizard":pg.integrate_website_page,
    "Tutorials": pg.tutorial_page,
    "Source Code": pg.src_code_page,
}

go_to = functions.get(st.session_state.current_page)
if go_to:
    go_to()
