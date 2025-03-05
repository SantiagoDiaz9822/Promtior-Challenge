# File: Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y curl

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and data
COPY src/ src/
COPY data/ data/

# Expose port for FastAPI
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]