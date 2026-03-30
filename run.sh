#!/bin/bash
set -e

echo "=== TITAN COMMAND v21 — Starting Services ==="

# 1. Start FastAPI on port 7860 (the ONLY publicly exposed port on HF Spaces)
echo "[1/2] Starting FastAPI backend on port 7860..."
uvicorn main:app --host 0.0.0.0 --port 7860 &
FASTAPI_PID=$!

# 2. Wait until FastAPI is confirmed ready
echo "[1/2] Waiting for FastAPI health check..."
for i in $(seq 1 20); do
  if curl -sf http://localhost:7860/ > /dev/null 2>&1; then
    echo "[1/2] ✅ FastAPI is ready on port 7860"
    break
  fi
  if [ $i -eq 20 ]; then
    echo "[1/2] ❌ FastAPI failed to start!"
    exit 1
  fi
  sleep 1
done

# 3. Start Streamlit dashboard on internal port 8000
echo "[2/2] Starting Streamlit dashboard on port 8000..."
streamlit run app.py \
  --server.port 8000 \
  --server.address 0.0.0.0 \
  --server.headless true \
  --browser.gatherUsageStats false &

echo "=== All services started ==="

# Keep container alive by waiting on the primary process (FastAPI)
wait $FASTAPI_PID