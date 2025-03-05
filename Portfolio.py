import streamlit as st

st.set_page_config(page_title="student portfolio", page_icon="🎓", layout="wide")

st.sidebar.title("📌 navigation")

page = st.sidebar.radio("Go to", ["Home","Project","Skills","Customize Profile","Contact"])