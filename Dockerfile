# Use a lightweight Python 3.11+ image
FROM python:3.11-slim

# Set working directory to the root of the project
WORKDIR /app

# Install system dependencies for GUI/Plotly if needed
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project structure
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir \
    fastapi \
    uvicorn \
    pydantic \
    streamlit \
    plotly \
    requests \
    pandas

# Set PYTHONPATH so the OpenEnv entrypoint resolves correctly
ENV PYTHONPATH="/app"

# Ensure the entrypoint script is executable
RUN chmod +x run.sh

# Expose the ports (8000 for FastAPI, 7860 for Streamlit/HF Spaces)
EXPOSE 8000 7860

# Launch the dual-process script
CMD ["./run.sh"]