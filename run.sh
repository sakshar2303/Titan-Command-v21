#!/bin/bash
echo "🚀 Starting TITAN BACKEND..."
# No 'cd' needed, main.py is right here
uvicorn main:app --host 0.0.0.0 --port 8000 &

sleep 3

echo "🛰️ Starting TITAN HUD..."
# No 'cd' needed, app.py is right here
streamlit run app.py --server.port 7860 --server.address 0.0.0.0