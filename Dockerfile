# Use a lighter base image
FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Set up the working directory
WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose ports for Ollama (11434) and FastAPI (8000)
EXPOSE 8000 11434

# Start Ollama server and FastAPI app
CMD sh -c "OLLAMA_NUM_PARALLEL=1 OLLAMA_MAX_LOADED_MODELS=1 ollama serve & sleep 20 && ollama pull tinyllama && uvicorn src.app:app --host 0.0.0.0 --port ${PORT:-8000}"