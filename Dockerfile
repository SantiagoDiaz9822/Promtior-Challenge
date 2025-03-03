# Use a base image with Python and Ubuntu
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Set up the working directory
WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose ports for Ollama (11434) and FastAPI (default: 8000)
EXPOSE 8000 11434

# Start Ollama server and FastAPI app
CMD sh -c "ollama serve & sleep 10 && ollama pull tinyllama && uvicorn src.app:app --host 0.0.0.0 --port ${PORT:-8000}"