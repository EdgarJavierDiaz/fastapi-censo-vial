import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app




from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_eventos():
    response = client.get("/eventos")
    assert response.status_code == 200
    