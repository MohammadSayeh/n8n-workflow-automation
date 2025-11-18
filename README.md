# 📰 Media Editing Automation System — n8n + Streamlit

This project provides a fully automated media-editing workflow using **n8n** as the backend automation engine and **Streamlit** as a clean, interactive frontend.

The system enables users to:

✅ Rewrite Arabic news text based on different editorial policies  
✅ Fetch English news from multiple international RSS feeds  
✅ Translate & filter incoming news using n8n + Gemini  
✅ Allow the user to choose any translated news article  
✅ Apply editing policies on the selected article dynamically  
✅ Compare raw news vs. edited version (clean layout)  
✅ Enjoy a modern, responsive UI built with Streamlit  

---

## 🌐 System Architecture

Below is the architecture used in this project:

Streamlit UI → n8n Webhooks → (LLM: Gemini) → JSON Output → Render in UI

---

## ✅ Features

### ✍️ **News Editor Module**
- User enters Arabic text manually.
- Selects one of 3 editorial policies:
  - **Najah Media**
  - **Gaza TV**
  - **Najah News**
- The system rewrites the text automatically through n8n → Gemini.
- Clean and readable output display.

---

### 🌍 **Translated World News Module**
- Fetches latest news from:
  - BBC
  - Washington Post
  - The Guardian
  - Al Jazeera
- Cleans & parses RSS XML through n8n.
- Filters news items using keyword-based classification.
- Translates each article using Gemini + Output Parser.
- Each article is displayed in a **modern card layout**:
  - Title (Arabic)
  - Description
  - Date
  - Source link
- User can **choose any article** and apply editorial policies to it.

---

## 🧠 Editorial Policies

Each policy applies a structured prompt engineered in n8n:

| Policy | Description |
|--------|-------------|
| **Najah Media** | Neutral, professional, academic tone |
| **Gaza TV** | National, human-focused, emotional tone |
| **Najah News** | Direct journalistic, chronological tone |

---

## 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| **n8n** | Workflows, news translation, filtering, LLM orchestration |
| **Google Gemini** | AI text generation and translation |
| **Streamlit** | Interactive frontend UI |
| **Python** | Data transformation and frontend logic |
| **RSS Feeds** | External news sources |

---

## 📌 How It Works (High-Level)

### 1️⃣ News Editing (User Text)
- User enters text → chooses policy → Streamlit sends request to n8n endpoint:
`/webhook-test/edit-text`

- n8n processes text through Gemini → returns JSON → displayed cleanly.

---

### 2️⃣ Fetch & Translate News
Streamlit calls:
`/webhook-test/english-news`

n8n does:
1. Fetches 4 international RSS feeds  
2. Cleans malformed XML  
3. Extracts `item` nodes  
4. Merges all feeds  
5. Filters based on keywords (Gaza, Palestine, occupation, etc.)  
6. Translates selected fields into Arabic  
7. Returns structured JSON  

---

## 🖼️ n8n Workflow Screenshot

<img width="1411" height="408" alt="image" src="https://github.com/user-attachments/assets/883ea4ce-df2d-47ab-ae9d-8534eb272cdd" />

## Demo video 
https://drive.google.com/file/d/1ZfjFrmoB9SAgYNhvaCxUvvagFdN34Jr9/view?usp=sharing

### 📂 Project Structure
```bash
📦 project/
 ┣ 📜 editor_app.py          # Main Streamlit app
 ┣ 📜 README.md               # Documentation
 ┣ 📂 workflows/              # n8n exported JSON workflows
 ┗ 📂 assets/                 # Optional images
```

### 🧩 Environment Requirements
✅ Python 3.10+
Install dependencies:

```bash
pip install streamlit requests
```

✅ n8n Installed Locally
Start n8n:

```bash
n8n start
```

Make sure your webhooks are reachable:

`/webhook-test/edit-text`

`/webhook-test/english-news`

### ▶️ Running the App
Start Streamlit:

```bash
streamlit run editor_app.py
```

The app will open automatically in the browser:

`http://localhost:8501`



### 👤 Author
Developed by Mohammad Sayeh

A fully automated editorial workflow integrating AI + automation + interactive UI.

---

