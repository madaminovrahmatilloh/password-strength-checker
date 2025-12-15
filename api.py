from fastapi import FastAPI
from pydantic import BaseModel
from core import analyze_password

app = FastAPI()

class PasswordRequest(BaseModel):
    password: str

@app.post("/check-password")
def check_password(req: PasswordRequest):
    data = analyze_password(req.password)
    return data