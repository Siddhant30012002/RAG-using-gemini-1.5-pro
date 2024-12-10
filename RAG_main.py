import streamlit as st
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS ## DB
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings ## Vector embedd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

pdf_path = r"C:\Users\HP\Desktop\MY_NLP_PROJECT\constitution\indian_constitution.pdf"

def get_doc():
    pdf_loader = PyPDFLoader(pdf_path)
    data = pdf_loader.load()
    return data 

def chunkking(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200,length_function=len)
    chunks = text_splitter.split_documents(data)
    return chunks

def embeddings(chunks):
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_DB = FAISS.from_documents(documents=chunks, embedding=embedding)
    return vector_DB

def Retriever(vector_DB):
    retriever = vector_DB.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return retriever

def LLM():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.3,max_tokens=300)
    return llm

def create_rag_chain(retriever, llm):
    # System prompt
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Use three sentences maximum and keep the answer concise.\n\n"
        "{context}"
    )

    # Setting up the prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )

    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)

    # Create the full RAG chain
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain


def main():
    st.title("Chat with PDF using the Gemini-1.5-Pro")

    # Load and prepare documents
    with st.spinner("Loading and preparing documents..."):
        data = get_doc()
        chunks = chunkking(data)
        vector_db = embeddings(chunks)
        retriever_instance = Retriever(vector_db)
        llm = LLM()
        rag_chain = create_rag_chain(retriever_instance, llm)

    # UI for user query
    user_query = st.text_input("Ask a question:")
    if user_query:
        with st.spinner("Generating response..."):
            response = rag_chain.invoke({"input": user_query})
            st.write(response.get("answer", "I don't know the answer."))


if __name__ == "__main__":
    main()