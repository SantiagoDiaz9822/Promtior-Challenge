#!/bin/sh
set -e

echo "Starting Ollama server..."
# Start the Ollama server in the background
ollama serve &
OLLAMA_PID=$!

# Wait a few seconds to allow Ollama to initialize
sleep 5

echo "Starting FastAPI server..."
# Use the Railway-supplied port if available, default to 8000
uvicorn src.app:app --host 0.0.0.0 --port ${PORT:-8000}

# Optionally wait on the Ollama process (this line may never be reached)
wait $OLLAMA_PID
