#!/bin/bash
echo "🚀 Starting TITAN BACKEND..."
# Run from the root folder
uvicorn main:app --host 0.0.0.0 --port 8000 &

sleep 5

echo "🛰️ Starting TITAN HUD..."
# Run from the root folder
streamlit run app.py --server.port 7860 --server.address 0.0.0.0