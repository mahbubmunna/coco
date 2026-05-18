from pydantic import BaseModel
from typing import Optional, Dict, Any

class IngestRequest(BaseModel):
    repo_path: str

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    
class SearchResult(BaseModel):
    file_path: str
    start_line: int
    end_line: int
    content: str
    similarity: float
