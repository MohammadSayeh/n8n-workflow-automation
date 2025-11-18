## 📝 Streamlit Editor + n8n Workflow Integration

### **🚀 Task Overview**

This Task integrates a **Streamlit** web interface with an **n8n Workflow Automation** system to create a smart text editor and comparison tool.
Users can input text via the Streamlit app, which is then processed through n8n using comparison and AI logic (Gemini API).

---

### **⚙️ Setup Instructions**

#### **1. Setting up the Streamlit Application**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/OppoTrainCommunity/n8n-workflows-tasks.git
    cd n8n-workflows-tasks
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run editor_app.py
    ```

4.  **Open your browser at:**
    ```arduino
    http://localhost:8501
    ```

#### **2. Running n8n Locally**



1.  **Install and run n8n:**
    ```bash
    npm install -g n8n
    n8n start
    ```

2.  **Then open in your browser:**
    ```arduino
    http://localhost:5678
    ```

#### **3. Importing the Workflow into n8n**

1.  Open n8n in your browser.
2.  Click **Import** $\rightarrow$ **From File**.
3.  Select the file **`workflow.json`** from the project folder.
4.  Click **Execute Workflow ▶️** to run it.

#### **4. Setting up Gemini API Key**

1.  Go to [https://aistudio.google.com/](https://aistudio.google.com/).
2.  Sign in with your Google account.
3.  Click **Get API Key** $\rightarrow$ **Create API key in new project**.
4.  Copy the key.
5.  **Inside n8n:**
    * Go to **Credentials** $\rightarrow$ **New** $\rightarrow$ **Gemini** (or use an **HTTP Request Node** if connecting directly).
    * Select **API Key Authentication**.
    * Paste your key in the provided field.
    * Save the credentials and link them to your node.

---

### **🖼️ Workflow Preview**

<img width="1491" height="571" alt="image" src="https://github.com/user-attachments/assets/4ea5b917-a0b4-4247-9822-a1f1da07dbcc" />




---

### **📌 Additional Notes**

* Both **Streamlit** and **n8n** must be running locally at the same time.
* Default ports: Streamlit $\rightarrow$ **8501**, n8n $\rightarrow$ **5678**.
* Ensure API endpoints in **`editor_app.py`** match your n8n server URL.
