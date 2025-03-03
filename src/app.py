from fastapi import FastAPI
from langserve import add_routes
from my_rag_pipeline import rag_chain  # Import your RAG chain

app = FastAPI(
    title="Promtior Chatbot API",
    description="API for Promtior's RAG-powered chatbot using Llama2 and Ollama",
)

# Add the RAG chain as an endpoint
add_routes(
    app,
    rag_chain,
    path="/promtior-chatbot",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)