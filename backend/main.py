"""
MindMirror AI - Main Application Entry Point
Initializes FastAPI, connects SQLite database, mounts API routes, and serves the Frontend SPA.
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .database.connection import init_db
from .api.routes import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB schemas on startup
    init_db()
    yield

app = FastAPI(
    title="MindMirror AI - Emotion-Aware Action Recommendation System",
    description="Machine Learning innovation system combining Transformer emotion analysis, intensity estimation, situational context extraction, and personalized next-step recommendations.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for local cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API endpoints
app.include_router(api_router)

# Mount Static Frontend
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/")
    async def serve_index():
        """Serves the main single-page application."""
        index_file = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"message": "MindMirror AI API is operational. Place frontend/index.html to view UI."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
