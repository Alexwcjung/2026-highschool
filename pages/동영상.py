import streamlit as st
import os

st.set_page_config(
    page_title="Video",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 영상 보기")

# =========================
# 영상 파일 목록
# GitHub의 videos 폴더 안 파일명과 정확히 일치해야 합니다.
# =========================
videos = {
    "영상 1": "videos/Streamlit_앱_활용_영어_수업 (1).mp4",
    "영상 2": "videos/video2.mp4",
    "영상 3": "videos/video3.mp4",
    "영상 4": "videos/video4.mp4",
}

tab1, tab2, tab3, tab4 = st.tabs(["영상 1", "영상 2", "영상 3", "영상 4"])

def show_video(title, path):
    st.subheader(title)

    if os.path.exists(path):
        st.video(path)
    else:
        st.error("영상 파일을 찾을 수 없습니다.")
        st.write("현재 찾고 있는 경로:")
        st.code(path)
        st.info("GitHub의 videos 폴더 안 파일명과 코드의 파일명이 정확히 같은지 확인하세요.")

with tab1:
    show_video("영상 1", videos["영상 1"])

with tab2:
    show_video("영상 2", videos["영상 2"])

with tab3:
    show_video("영상 3", videos["영상 3"])

with tab4:
    show_video("영상 4", videos["영상 4"])
