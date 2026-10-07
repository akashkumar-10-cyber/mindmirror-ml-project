"""
MindMirror AI - Database Connection Module
Configures SQLite with SQLAlchemy ORM.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database path in the project root or backend folder
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "..", "..", "mindmirror.db")
DB_PATH = os.path.abspath(DB_PATH)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency that provides an independent database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Create all database tables on application launch."""
    from . import models
    Base.metadata.create_all(bind=engine)

# Auto-initialize tables on module import
init_db()
