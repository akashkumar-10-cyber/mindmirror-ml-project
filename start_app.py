"""
MindMirror AI - Application Launcher
Starts the FastAPI backend and serves the frontend on http://127.0.0.1:8000.
"""

import os
import sys
import time
import webbrowser
import threading
import uvicorn

def open_browser():
    """Opens browser after server startup."""
    time.sleep(1.5)
    url = "http://127.0.0.1:8000"
    print(f"\n[MindMirror AI] Opening browser at {url} ...")
    try:
        webbrowser.open(url)
    except Exception:
        pass

def print_banner():
    banner = r"""
================================================================================
   __  __ _           _ __  __ _                     _    ___ 
  |  \/  (_)_ __   __| |  \/  (_)_ __ _ __ ___  _ __ / \  |_ _|
  | |\/| | | '_ \ / _` | |\/| | | '__| '__/ _ \| '__/ _ \  | | 
  | |  | | | | | | (_| | |  | | | |  | | | (_) | | / ___ \ | | 
  |_|  |_|_|_| |_|\__,_|_|  |_|_|_|  |_|  \___/|_|/_/   \_\___|
                                                                
  Emotion-Aware Action Recommendation & Wellness Support System
================================================================================
  [ML Architecture] HuggingFace DistilRoBERTa + PyTorch + FastAPI + SQLite
  [Status]           Server launching on: http://127.0.0.1:8000
  [Frontend]         Web UI available at: http://127.0.0.1:8000
  [API Docs]         Swagger UI docs at:  http://127.0.0.1:8000/docs
================================================================================
    """
    print(banner)

def main():
    print_banner()

    # Pre-warm DB and ML Model
    print("[1/2] Initializing SQLite database and pre-warming ML model...")
    try:
        from backend.database.connection import init_db
        from backend.ml.emotion_model import emotion_classifier
        init_db()
        print(f"      Loaded model: {emotion_classifier.model_name}")
    except Exception as ex:
        print(f"      Startup notice: {ex}")

    print("[2/2] Launching Uvicorn ASGI Server...")
    print("\n >>> MindMirror AI is running! Click or open in browser: http://127.0.0.1:8000 <<<\n")

    # Start browser opener in background thread
    threading.Thread(target=open_browser, daemon=True).start()

    # Start Uvicorn server
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, log_level="info", reload=False)

if __name__ == "__main__":
    main()
