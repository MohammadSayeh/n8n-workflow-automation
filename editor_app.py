import streamlit as st
import requests
import json


st.set_page_config(page_title="نظام التحرير الإعلامي", layout="wide", page_icon="📰")


EDIT_ENDPOINT = "http://localhost:5678/webhook-test/edit-text"
NEWS_ENDPOINT = "http://localhost:5678/webhook-test/english-news"

CUSTOM_CSS = """
<style>
.stApp { background-color:#f5f7fa; }
.card {
    background:white;
    padding:1.2rem;
    border-radius:12px;
    border:1px solid #e5eaf0;
    box-shadow:0 2px 12px rgba(0,0,0,0.06);
    margin-bottom:1rem;
}
.badge {
    padding:3px 8px;
    background:#e8f0fe;
    border:1px solid #c7d7fe;
    border-radius:20px;
    color:#1a56db;
    font-size:12px;
}
.mono {
    font-family:monospace;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)



#  Session State

if "edited_text" not in st.session_state:
    st.session_state.edited_text = None

if "selected_news" not in st.session_state:
    st.session_state.selected_news = None

if "news_list" not in st.session_state:
    st.session_state.news_list = []

if "edited_news_text" not in st.session_state:
    st.session_state.edited_news_text = None



# helper functions

def post_edit_text(policy: str, text: str):
    try:
        resp = requests.post(EDIT_ENDPOINT, json={"policy": policy, "text": text}, timeout=60)
        resp.raise_for_status()

        try:
            data = resp.json()
            if isinstance(data, list):
                return data[0].get("text") or data[0].get("output")
            elif isinstance(data, dict):
                return data.get("text") or data.get("output")
            return resp.text
        except:
            return resp.text
    except Exception as e:
        st.error(f"خطأ في وورك فلو التحرير: {e}")
        return None


def fetch_news():
    try:
        resp = requests.post(NEWS_ENDPOINT, timeout=60)
        resp.raise_for_status()

        raw = resp.json()
        out = []

        for item in raw:
            block = item.get("output", item)
            out.append({
                "title_ar": block.get("title_ar", ""),
                "description_ar": block.get("description_ar", ""),
                "source_link": block.get("source_link", ""),
                "date": block.get("date", ""),
            })

        return out

    except Exception as e:
        st.error(f"خطأ أثناء جلب الأخبار: {e}")
        return []


def unify_news_text(item):
    """تحويل الخبر إلى نص موحد لإرساله إلى وورك فلو التحرير"""
    return f"""
العنوان: {item['title_ar']}

الوصف: {item['description_ar']}

التاريخ: {item['date']}

المصدر: {item['source_link']}
"""




st.title("📰 نظام التحرير الإعلامي")

tab1, tab2 = st.tabs(["✍️ محرّر الأخبار", "🌍 الأخبار العالمية"])



with tab1:
    st.subheader("✍️ أدخل نصًا واختر سياسة تحريرية")

    user_text = st.text_area("النص الأصلي:", height=200)

    col1, col2, col3 = st.columns(3)

    if col1.button("🔹 سياسة Najah Media", disabled=not user_text.strip()):
        with st.spinner("يتم التطبيق..."):
            st.session_state.edited_text = post_edit_text("Najah Media", user_text)

    if col2.button("🔹 سياسة Gaza TV", disabled=not user_text.strip()):
        with st.spinner("يتم التطبيق..."):
            st.session_state.edited_text = post_edit_text("Gaza TV", user_text)

    if col3.button("🔹 سياسة Najah News", disabled=not user_text.strip()):
        with st.spinner("يتم التطبيق..."):
            st.session_state.edited_text = post_edit_text("Najah News", user_text)

    if st.session_state.edited_text:
        st.markdown("### ✅ النص بعد التحرير")
        st.markdown(f"<div class='card mono'>{st.session_state.edited_text}</div>", unsafe_allow_html=True)



with tab2:
    st.subheader("🌍 جلب الأخبار العالمية المترجمة")

    if st.button("🌐 جلب الأخبار"):
        with st.spinner("جاري جلب الأخبار..."):
            st.session_state.news_list = fetch_news()
            st.session_state.selected_news = None
            st.session_state.edited_news_text = None

    news = st.session_state.news_list

    if news:
        st.success(f"✅ تم جلب {len(news)} خبرًا")

        st.markdown("### 🗞️ جميع الأخبار المترجمة:")

        for i, item in enumerate(news):
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.markdown(f"### {i+1}- {item['title_ar']}")
            st.markdown(f"**📄 الوصف:** {item['description_ar']}")
            st.markdown(f"**📅 التاريخ:** {item['date']}")
            st.markdown(f"**🔗 المصدر:** [اضغط هنا]({item['source_link']})")

            if st.button(f"✅ اختيار هذا الخبر", key=f"choose_{i}"):
                st.session_state.selected_news = item
                st.session_state.edited_news_text = None

            st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.selected_news:
        st.markdown("### ✅ الخبر المختار:")
        st.markdown(f"<div class='card'>{unify_news_text(st.session_state.selected_news)}</div>", unsafe_allow_html=True)

        st.markdown("### اختر سياسة لتحرير هذا الخبر:")

        c1, c2, c3 = st.columns(3)

        base_text = unify_news_text(st.session_state.selected_news)

        if c1.button("🔹 Najah Media"):
            with st.spinner("يتم التطبيق..."):
                st.session_state.edited_news_text = post_edit_text("Najah Media", base_text)

        if c2.button("🔹 Gaza TV"):
            with st.spinner("يتم التطبيق..."):
                st.session_state.edited_news_text = post_edit_text("Gaza TV", base_text)

        if c3.button("🔹 Najah News"):
            with st.spinner("يتم التطبيق..."):
                st.session_state.edited_news_text = post_edit_text("Najah News", base_text)

        if st.session_state.edited_news_text:
            st.markdown("### ✅ الناتج بعد تطبيق السياسة")
            st.markdown(f"<div class='card mono'>{st.session_state.edited_news_text}</div>", unsafe_allow_html=True)
