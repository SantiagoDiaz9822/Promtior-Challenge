# Use an official Python runtime as the base image
FROM python:3.10-slim

# Ensure Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh
# Expose the port that the application listens on
EXPOSE 8000

# Start the application using the entrypoint script
CMD ["./entrypoint.sh"]
