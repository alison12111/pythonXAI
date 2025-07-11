import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 載入.env檔案內容

openai.api_key = os.getenv("OPENAI_API_KEY")

if "history" not in st.session_state:
    st.session_state.history = []

if "system_message" not in st.session_state:  # 初始化系統訊息
    # 如果系統訊息不存在,設置系統預設訊息
    st.session_state.system_message = "請用繁體中文進行對話"

# 設置三個列布局,分別占用6:1的寬度
col1, col2 = st.columns([6, 1])
with col1:
    # 在一列顯示並更新系統訊息
    st.session_state.system_message = st.text_input(
        "請輸入系統訊息", st.session_state.system_message
    )

with col2:
    if st.button("💖"):  # 在第三列顯示清空按鈕
        st.session_state.history = []  # 按下按鈕後清空對話紀錄
        st.rerun()  # 重新整理頁面已反映更新

# 從對話紀錄中送代每個訊息並顯示
for message in st.session_state.history:
    if message["role"] == "user":  # 如果訊息的腳色是使用者
        st.chat_message("user", avatar="♉").write(message["content"])
        # 顯示使用者的訊息,使用者指定的頭像
    else:
        st.chat_message("assistant", avatar="🔯").write(message["content"])
        # 顯示AI的訊息,AI指定的頭像

prompt = st.chat_input("請輸入你的訊息")  # 顯示對話輸入框,等待使用者輸入訊息
if prompt:  # 如果有訊息輸入
    st.session_state.history.append({"role": "user", "content": prompt})
    # 將使用者的訊息加入對話紀錄

    response = openai.chat.completions.create(
        model="gpt-4o-mini-search-preview",  # 使用選定AI模型
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )
    assistant_message = response.choices[0].message.content  # 取得AI駐守回傳訊息內容
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    # 將AI的回傳訊息加入對話紀錄
    st.rerun()  # 重新整理頁面已顯示新的訊息
