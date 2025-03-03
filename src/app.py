from fastapi import FastAPI
from langserve import add_routes
from src.my_rag_pipeline import rag_chain  # Ensure this import is correct
import uvicorn
import argparse

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
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    parser.add_argument("--port", type=int, default=8000, help="Port number")
    args = parser.parse_args()

    # Start the Uvicorn server
    uvicorn.run("app:app", host=args.host, port=args.port, reload=True)