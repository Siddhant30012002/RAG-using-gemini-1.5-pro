
# Chat with PDF using Gemini-1.5-Pro 

This application allows you to interact with a PDF document by asking questions and receiving concise, context-aware answers. Built with **LangChain**, **FAISS**, and **Google Generative AI** models, it leverages advanced Retrieval-Augmented Generation (RAG) techniques to deliver an efficient Q&A experience.

---

## Features

- **Document Parsing**: Load and preprocess PDF files for NLP tasks.  
- **Efficient Retrieval**: Uses FAISS for vector-based document retrieval with embeddings.  
- **AI-Powered Chat**: Integrated with **Gemini-1.5-Pro** for intelligent and context-aware responses.  
- **Customizable Components**: Modular design allows for flexible text chunking, retrieval, and LLM configuration.  
- **Streamlit Interface**: Simple and interactive front-end for seamless user experience.  

---

## Prerequisites

Ensure you have the following installed:
- Python 3.10 or later
- Pip for package management

Install all required libraries using:
```bash
pip install -r requirements.txt
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/chat-with-pdf.git
   cd chat-with-pdf
   ```

2. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add the following keys:
     ```
     GOOGLE_GENERATIVE_API_KEY=<your_api_key_here>
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

---


---

## How It Works

### 1. **PDF Loading**
The `get_doc()` function uses `PyPDFLoader` to parse the document and load its content into memory.

### 2. **Chunking Text**
The `chunkking(data)` function splits the document into manageable pieces using `RecursiveCharacterTextSplitter`.

### 3. **Embedding Creation**
The `embeddings(chunks)` function uses **GoogleGenerativeAIEmbeddings** to generate embeddings for each chunk and store them in a FAISS vector database.

### 4. **Retrieval**
The `Retriever(vector_DB)` function retrieves the most relevant document chunks based on user queries.

### 5. **Language Model**
The `LLM()` function initializes **ChatGoogleGenerativeAI** using the `Gemini-1.5-Pro` model for intelligent responses.

### 6. **RAG Chain**
The `create_rag_chain()` function combines retrieval and language model capabilities into a cohesive RAG pipeline.

---

## Usage

1. **Start the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Upload PDF and Ask Questions**:
   - Load your PDF file.
   - Type your question in the input box.
   - View the AI-generated response in real-time.

---

## Technologies Used

- **LangChain**: For chaining retrieval and language models.  
- **FAISS**: For vector-based similarity search.  
- **Google Generative AI**: To generate embeddings and provide intelligent answers.  
- **Streamlit**: For building the user interface.  
- **PyPDFLoader**: For PDF parsing.

---


## Future Enhancements

-  Support for multi-file document search.  
-  Deploy to cloud platforms like AWS, Azure, or GCP.  
-  Add support for more LLMs and embeddings.  

---


## Contact

For any questions or feedback, feel free to reach out:

- **Email**: siddhantkadiyal08@gmail.com  
- **LinkedIn**: [www.linkedin.com/in/siddhant-kadiyal]
- **GitHub**: (https://github.com/Siddhant30012002)

--- 
