#!/bin/bash
# Put the Backend on 7860 so the Public URL hits it directly
uvicorn main:app --host 0.0.0.0 --port 7860 &

sleep 5

# Put the Streamlit HUD on 8000
streamlit run app.py --server.port 8000 --server.address 0.0.0.0