app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://crm-auth-1.onrender.com"],  # в проде укажи домен фронта
    ...
)
