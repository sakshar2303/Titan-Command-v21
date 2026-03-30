#!/bin/bash
# Start FastAPI on port 7860 (the only port HF Spaces exposes publicly)
uvicorn main:app --host 0.0.0.0 --port 7860 &
FASTAPI_PID=$!

# Wait for FastAPI to be ready before starting Streamlit
echo "Waiting for FastAPI to start..."
for i in $(seq 1 15); do
  if curl -s http://localhost:7860/status > /dev/null 2>&1; then
    echo "FastAPI is ready on port 7860"
    break
  fi
  sleep 1
done

# Start Streamlit on a separate internal port (not publicly exposed)
streamlit run app.py --server.port 8000 --server.address 0.0.0.0 &

# Keep the container alive by waiting on the FastAPI process
wait $FASTAPI_PID