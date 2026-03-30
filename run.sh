#!/bin/bash

# 1. Find where main.py actually is
MAIN_PATH=$(find /app -name "main.py" | head -n 1)
APP_PATH=$(find /app -name "app.py" | head -n 1)

# Get the directories
BACKEND_DIR=$(dirname "$MAIN_PATH")
FRONTEND_DIR=$(dirname "$APP_PATH")

echo "📂 Found Backend at: $BACKEND_DIR"
echo "📂 Found Frontend at: $FRONTEND_DIR"

# 2. Start the TITAN BACKEND
echo "🚀 Starting TITAN BACKEND..."
cd "$BACKEND_DIR"
uvicorn main:app --host 0.0.0.0 --port 8000 &

# 3. Give it a head start
sleep 3

# 4. Start the TITAN HUD
echo "🛰️ Starting TITAN HUD..."
cd "$FRONTEND_DIR"
streamlit run app.py --server.port 7860 --server.address 0.0.0.0