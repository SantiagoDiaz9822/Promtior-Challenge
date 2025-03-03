# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make entrypoint.sh executable
RUN chmod +x entrypoint.sh

# Expose the port that the app runs on (Railway uses the PORT environment variable)
EXPOSE 8000

# Run the entrypoint script
CMD ["./entrypoint.sh"]
