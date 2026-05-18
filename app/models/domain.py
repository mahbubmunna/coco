from sqlalchemy import Column, String, Integer, Text, JSON
from pgvector.sqlalchemy import Vector
from app.core.db import Base

class CodeChunk(Base):
    __tablename__ = "code_chunks"

    id = Column(Integer, primary_key=True, index=True)
    repo_path = Column(String, index=True)
    file_path = Column(String, index=True)
    start_line = Column(Integer)
    end_line = Column(Integer)
    content = Column(Text)
    # BAAI/bge-small-en-v1.5 produces 384-dimensional embeddings
    embedding = Column(Vector(384)) 
    metadata_json = Column(JSON, default={})
