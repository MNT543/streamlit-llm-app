from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# =========================
# LLM関数
# =========================
def get_llm_response(user_input, role_type):
    # 役割ごとにシステムメッセージを切り替え
    if role_type == "動物の習性":
        system_message = "あなたは動物の習性に詳しい専門家です。わかりやすく解説してください。"
    else:
        system_message = "あなたは動物に与えるおすすめのえさに詳しい専門家です。具体的に提案してください。"

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5
    )

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content

# =========================
# UI
# =========================
st.title(" 動物専門AIアプリ")

# アプリ説明
st.write("""
このアプリでは、動物について質問するとAIが専門家として回答します。

【使い方】
1. 専門家の種類を選択
2. 動物の名前を入力
3. 「送信」ボタンをクリック
""")

# ラジオボタン
role = st.radio(
    "専門家の種類を選択してください",
    ("動物の習性", "動物に与えるおすすめのえさ")
)

# 入力フォーム
user_input = st.text_input("質問を入力してください")

# ボタン
if st.button("送信"):
    if user_input:
        with st.spinner("考え中..."):
            result = get_llm_response(user_input, role)
        st.subheader("回答")
        st.write(result)
    else:
        st.warning("テキストを入力してください")