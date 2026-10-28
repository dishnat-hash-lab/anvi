import streamlit as st
import time

st.set_page_config(
    page_title="Happy Anniversary, Mom & Dad ❤️",
    page_icon="❤️",
    layout="centered",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff7f7 0%, #ffe9ef 50%, #fff8f0 100%);
}
.hero {
    text-align: center;
    padding: 35px 15px 15px;
}
.title {
    font-size: 48px;
    font-weight: 800;
    color: #8f2147;
    margin-bottom: 8px;
}
.subtitle {
    font-size: 22px;
    color: #6f4655;
}
.card {
    background: rgba(255,255,255,0.82);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 8px 30px rgba(120, 50, 75, 0.12);
    margin: 20px 0;
}
.message {
    font-size: 21px;
    line-height: 1.8;
    color: #49343c;
    text-align: center;
}
.footer {
    text-align: center;
    color: #7b5964;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div style="font-size:70px;">❤️ 💐 ❤️</div>
    <div class="title">Happy Anniversary, Mummy& Daddy!</div>
</div>
""", unsafe_allow_html=True)

if "show" not in st.session_state:
    st.session_state.show = False

if st.button("💌 Open Your Anniversary Message", use_container_width=True):
    st.session_state.show = True
    st.balloons()

if st.session_state.show:
    st.markdown("""
    <div class="card">
        <div class="message">
        Dear Mom & Dad,<br><br>
        Happy Anniversary ❤️<br><br>
        Thank you both for shaping me into the man I am today. 
        Everyday I am grateful for your support and kindness. Wishing you endless happiness on your special day and forever! 
        <br><br>
        <b>Here's to your love, your memories, and all the years still to come.</b>
        <br><br>
        With lots of love,<br>
        <b>Your Son ❤️</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="message">
        🌹 <b>One wish for you both:</b><br>
        May every coming year be even happier than the last one.
        </div>
    </div>
    """, unsafe_allow_html=True)

