
import streamlit as st

st.set_page_config(page_title="Video Learning", page_icon="🎬", layout="wide")

st.title("🎬 동영상 수업")

video_path = "videos/Streamlit_앱_활용_영어_수업 (1).mp4"

st.video(video_path)
