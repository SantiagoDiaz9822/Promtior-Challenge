# File: src/my_rag_pipeline.py
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings  # Open-source embeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaEmbeddings, OllamaLLM

# Load and Split Data
loader = TextLoader("data/combined_data.txt", encoding="utf-8")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
splits = text_splitter.split_documents(docs)

# Create Vector Store
embeddings = OllamaEmbeddings(
    model="llama2:7b",
    base_url="http://ec2-3-85-233-72.compute-1.amazonaws.com:11434"  # Local Ollama server (It should be running)
)


vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever()

# Build RAG Pipeline
# Initialize Llama2 via Ollama 
llm = OllamaLLM(
    model="llama2:7b",
    base_url="http://ec2-3-85-233-72.compute-1.amazonaws.com:11434"  # Local Ollama server (It should be running)
)

# Define the prompt template
prompt = ChatPromptTemplate.from_template(
    """Answer the question using ONLY the context below. Be concise.
    
    Context: {context}
    
    Question: {input}
    
    Answer:"""
)

# Build the RAG chain
rag_chain = (
    {"context": retriever, "input": RunnablePassthrough()}
    | prompt
    | llm
)
