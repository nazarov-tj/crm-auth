from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import random, string, jwt
from datetime import datetime, timedelta

router = APIRouter()

OTP_STORE = {}
SECRET_KEY = "supersecret"

class LoginRequest(BaseModel):
    email: EmailStr

class VerifyRequest(BaseModel):
    email: EmailStr
    code: str

@router.post("/request-code")
def request_code(data: LoginRequest):
    code = ''.join(random.choices(string.digits, k=6))
    OTP_STORE[data.email] = code
    print(f"OTP for {data.email}: {code}")
    return {"message": "Code sent"}

@router.post("/verify")
def verify_code(data: VerifyRequest):
    real_code = OTP_STORE.get(data.email)
    if real_code != data.code:
        raise HTTPException(status_code=400, detail="Invalid code")
    token = jwt.encode(
        {"sub": data.email, "exp": datetime.utcnow() + timedelta(hours=1)},
        SECRET_KEY,
        algorithm="HS256"
    )
    return {"access_token": token}