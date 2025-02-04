---

# **RAG Q&A Conversation With PDF Including Chat History**  

## 📌 Overview  
This project implements a **Conversational RAG (Retrieval-Augmented Generation)** model that allows users to **upload PDFs** and interact with their content through a chat interface. It maintains **chat history**, enhances question contextualization, and provides accurate answers using **LangChain, ChromaDB, and Groq API**.  

## 🚀 Features  
✅ Upload multiple **PDF files** and extract their content  
✅ Utilize **Retrieval-Augmented Generation (RAG)** for accurate answers  
✅ Maintain **chat history** for contextual conversation  
✅ Leverage **Hugging Face embeddings & ChromaDB** for document retrieval  
✅ Secure API key input for **Groq LLM (Gemma2-9b-It)**  
✅ Deployable with **Streamlit & Docker**  

## 🛠️ Tech Stack  
- **Python** (Streamlit, LangChain, ChromaDB)  
- **LLMs** (Groq API with Gemma2-9b-It)  
- **Embeddings** (Hugging Face `all-MiniLM-L6-v2`)  
- **Document Processing** (PyPDFLoader, Recursive Text Splitter)  
- **Session Management** (Streamlit's `session_state`)  

## 📂 Installation & Setup  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Rupeshsingh4253/Generative_AI.git
cd Generative_AI
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**  
Create a `.env` file and add your Hugging Face & Groq API keys:  
```env
HF_TOKEN=your_huggingface_api_key
GROQ_API_KEY=your_groq_api_key
```

### **4️⃣ Run the Application**  
```sh
streamlit run app.py
```

## 🎯 How It Works  
1️⃣ Upload PDF files  
2️⃣ Ask questions about the uploaded content  
3️⃣ The system retrieves relevant document chunks  
4️⃣ The **RAG model** generates a precise answer  
5️⃣ The chat history maintains context for better responses  

## 🖥️ Demo  
[![Watch the video](https://img.youtube.com/vi/your_video_id/maxresdefault.jpg)](https://youtu.be/your_video_id)  

## 📌 Folder Structure  
```
📁 Generative_AI
│-- 📂 4-RAG Documents       # PDF Processing Code  
│-- 📜 app.py                # Streamlit App  
│-- 📜 requirements.txt       # Dependencies  
│-- 📜 .env                   # API Keys (Ignored in Git)  
│-- 📜 README.md              # Project Documentation  
```

## 🔗 Useful Links  
- 📝 **Project Repository**: [GitHub](https://github.com/Rupeshsingh4253/Generative_AI)  
- 📄 **LangChain Docs**: [LangChain](https://python.langchain.com/)  
- 📚 **ChromaDB**: [ChromaDB](https://github.com/chroma-core/chroma)  
- 🤗 **Hugging Face**: [HuggingFace Models](https://huggingface.co/)  

## 🤝 Contributing  
Feel free to **fork**, **contribute**, and **submit PRs**! 😊  

---
