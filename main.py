import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
import openai
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Uncomment if using OpenAI embeddings
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Set GROQ API Key
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the LLM (Groq model)
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Define the chat prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Question: {input}
    """
)

# Create vector embeddings for documents
def create_vector_embedding():
    if "vectors" not in st.session_state:
        # Initialize session state variables if they don't exist
        st.session_state.embeddings = OpenAIEmbeddings()  # Ensure your OpenAI API key is set
        st.session_state.loader = PyPDFDirectoryLoader("research_papers")  # Data Ingestion
        st.session_state.docs = st.session_state.loader.load()  # Load documents
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("RAG Document Q&A With Groq and Llama3")

user_prompt = st.text_input("Enter your query related to the research paper")

if st.button("Create Document Embeddings"):
    with st.spinner("Creating vector embeddings..."):
        create_vector_embedding()
        st.success("Vector Database is ready!")

if user_prompt:
    # Ensure the "vectors" state is initialized
    if "vectors" not in st.session_state:
        st.warning("Please create the document embeddings first.")
    else:
        # Create the retrieval chain
        with st.spinner("Processing your request..."):
            try:
                document_chain = create_stuff_documents_chain(llm, prompt)
                retriever = st.session_state.vectors.as_retriever()
                retrieval_chain = create_retrieval_chain(retriever, document_chain)

                start_time = time.process_time()
                response = retrieval_chain.invoke({'input': user_prompt})
                st.write(f"Response time: {time.process_time() - start_time:.2f} seconds")

                st.write(response['answer'])

                # Display document similarity search results in an expander
                with st.expander("Document Similarity Search"):
                    for i, doc in enumerate(response['context']):
                        st.write(doc.page_content)
                        st.write('------------------------')

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
