import streamlit as st
import requests
import json
import difflib

st.set_page_config(page_title="نظام التحرير الإعلامي", layout="wide")
st.title("📰 نظام التحرير الإعلامي")
st.write("أدخل نصك أدناه ثم اختر السياسة التحريرية:")

user_text = st.text_area("النص الأصلي:", height=200)

col1, col2, col3 = st.columns(3)
edited_text = None

webhook_url = "http://localhost:5678/webhook-test/edit-text"

def send_request(policy):
    
    try:
        response = requests.post(webhook_url, json={"policy": policy, "text": user_text})
        response.raise_for_status()
        try:
            result_json = response.json()
            if isinstance(result_json, list) and "text" in result_json[0]:
                return result_json[0]["text"]
            else:
                return response.text
        except json.JSONDecodeError:
            return response.text
    except Exception as e:
        st.error(f"حدث خطأ أثناء الاتصال بـ n8n: {e}")
        return None

with col1:
    if st.button("🔹 سياسة Najah Media"):
        edited_text = send_request("Najah Media")
with col2:
    if st.button("🔹 سياسة Gaza TV"):
        edited_text = send_request("Gaza TV")
with col3:
    if st.button("🔹 سياسة Najah News"):
        edited_text = send_request("Najah News")

if edited_text:
    st.subheader("📑 النص المحرر (منسق):")
    st.markdown(edited_text)  

    st.subheader("🔍 مقارنة النصوص:")
    diff_html = ""
    diff = difflib.ndiff(user_text.splitlines(), edited_text.splitlines())
    for line in diff:
        if line.startswith("+ "):
            diff_html += f'<div style="background-color:#e6ffe6;">{line[2:]}</div>'
        elif line.startswith("- "):
            diff_html += f'<div style="color:#ff0000;">{line[2:]}</div>'
        else:
            diff_html += f"<div>{line[2:]}</div>"

    st.markdown(diff_html, unsafe_allow_html=True)
