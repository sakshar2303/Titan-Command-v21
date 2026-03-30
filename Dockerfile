# Use a lightweight Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (curl needed for health check in run.sh)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set PYTHONPATH so imports resolve correctly
ENV PYTHONPATH="/app"

# Ensure the entrypoint script is executable
RUN chmod +x run.sh

# Expose port 7860 (FastAPI - publicly accessible on HF Spaces)
# and port 8000 (Streamlit - internal dashboard)
EXPOSE 7860 8000

# Launch via the startup script
CMD ["./run.sh"]