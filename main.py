# app/main.py
from __future__ import annotations

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import company, login, news, user

app = FastAPI()

# Set all CORS enabled origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router, tags=["Users"])
app.include_router(company.router, tags=["Company"])
app.include_router(news.router, tags=["News"])
app.include_router(login.router, tags=["Login"])
