app.add_middleware(
    CORSMiddleware,
    allow_origins=["*nazarov-tj"],  # в проде укажи домен фронта
    ...
)
