
# 💬 RAG Complaint Chatbot

A conversational AI chatbot built using Streamlit and FastAPI. It can register customer complaints and answer policy-related questions using Retrieval-Augmented Generation (RAG) from a PDF-based knowledge base.

## 📁 Project Structure

```
rag_chatbot/
├── backend/
│   ├── main.py              
│   ├── db.py                
│   ├── models.py            
│   ├── schemas.py            
│   ├── rag_knowledge.py    
├── frontend/
│   └── app.py                
├── knowledge_base/
│   └── policies.pdf         
├── requirements.txt
├── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag_chatbot.git
cd rag_chatbot
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the App

### Step 1: Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Check it at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Step 2: Start Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Open [http://localhost:8501](http://localhost:8501) to use the chatbot.

---

## 🧪 Example Interaction

```
User: I want to file a complaint about a delayed delivery.
Bot: I'm sorry to hear that. Please provide your name.
...
Bot: Your complaint has been registered with ID: XYZ123
```

---

## 📝 License

MIT License. Feel free to fork and customize!
