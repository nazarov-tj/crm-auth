app.add_middleware(
    CORSMiddleware,
    allow_origins=["frontend-jb2s.onrender.com"],  # в проде укажи домен фронта
    ...
)
