#!/bin/bash
# Start the backend on the MAIN port (7860) so the URL hits it directly
uvicorn main:app --host 0.0.0.0 --port 7860 &

sleep 3

# Start Streamlit on a different port (8000)
streamlit run app.py --server.port 8000 --server.address 0.0.0.0