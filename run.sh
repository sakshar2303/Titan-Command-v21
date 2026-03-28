#!/bin/bash

# 1. Start the FastAPI Backend in the background
echo "🚀 Starting TITAN BACKEND..."
cd titan-command-v8/backend && uvicorn main:app --host 0.0.0.0 --port 8000 &

# 2. Wait a moment for the backend to warm up
sleep 3

# 3. Start the Streamlit Frontend in the foreground
echo "🛰️ Starting TITAN HUD..."
cd ../frontend && python3 -m streamlit run app.py --server.port 7860 --server.address 0.0.0.0