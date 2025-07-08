import streamlit as st

# st.number_input()#可以讓使用者輸入數字，可以逕行以下設定
# step=1可以讓使用者輸入整數
# min_value=0可以可以設定最小值為0
# max_value=10可以設定最大值為100
number = st.number_input("請輸入數字：", step=1, min_value=0, max_value=100)
# 顯示使用者輸入的數字
st.write(f"你輸入的數字是:{number}")

st.write("## 練習")
score = st.number_input("請輸入你的分數：", step=1, min_value=0, max_value=100)
if score >= 90:
    st.write("你的成績很好！")
elif score >= 80:
    st.write("你的成績一般")
elif score >= 70:
    st.write("你的成績不好")
elif score >= 60:
    st.write("你的成績不太好")
else:
    st.write("你的成績很差")
