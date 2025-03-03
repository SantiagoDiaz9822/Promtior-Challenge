# File: src/rag_pipeline.py
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings  # Open-source embeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# --------------------------
# Step 1: Load and Split Data
# --------------------------
loader = TextLoader("../data/combined_data.txt", encoding="utf-8")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
splits = text_splitter.split_documents(docs)

# --------------------------
# Step 2: Create Vector Store
# --------------------------
# Use open-source embeddings (no API key needed)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever()

# --------------------------
# Step 3: Build RAG Pipeline
# --------------------------
# Initialize Llama2 via Ollama
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama2")  # Uses local Ollama server

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

# --------------------------
# Step 4: Test the Pipeline
# --------------------------
# Start Ollama server in the background first!
# Run this in a separate terminal: `ollama serve`

if __name__ == "__main__":
    # Ensure Ollama is running in the background first!
    # Run `ollama serve` in a separate terminal

    # Test questions
    questions = [
        "When was promtior founded?",
        "What services does promtior offer?",
    ]

    for question in questions:
        print(f"\nQuestion: {question}")
        response = rag_chain.invoke(question)
        print(f"Answer: {response}")