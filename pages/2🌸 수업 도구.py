# =========================
# 선생님께 부탁해요 탭
# 저장이 불안정한 도화지/게시판 기능은 제거하고,
# 구글닥 바로가기만 남긴 단순 버전입니다.
# =========================

with tabs[-1]:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #eff6ff 0%, #fdf4ff 45%, #fff7ed 100%);
            border: 1.5px solid #c4b5fd;
            border-radius: 28px;
            padding: 26px 24px;
            box-shadow: 0 8px 22px rgba(124,58,237,0.12);
            margin-bottom: 18px;
        ">
            <div style="font-size:34px; font-weight:900; color:#312e81; margin-bottom:10px;">
                🙋 선생님께 부탁해요
            </div>
            <div style="font-size:18px; font-weight:800; color:#475569; line-height:1.7;">
                수업 중 듣고 싶은 노래, 하고 싶은 활동, 선생님께 부탁하고 싶은 내용을 자유롭게 적어 주세요.<br>
                아래 버튼을 누르면 구글 문서로 이동합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "📝 선생님께 부탁하러 가기",
        "https://docs.google.com/document/d/1kjXveuOIiRQnrcWiyvSsS0DeXSqEe4bphDr0_DSkQyk/edit?tab=t.0",
        use_container_width=True
    )

    st.caption("※ 구글 문서에 적은 내용은 자동 저장됩니다. 단, 구글 문서 공유 설정이 '링크가 있는 모든 사용자 편집 가능'이어야 학생들이 쓸 수 있습니다.")
