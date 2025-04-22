# CRM Auth Module (FastAPI + React)

## 📦 Состав проекта
- **Backend**: FastAPI (OTP Login, JWT)
- **Frontend**: React (Tailwind UI)
- **Deploy**: Render.com
- **DB**: SQLite/Postgres (опционально)

---

## 🚀 Как развернуть на Render.com

### 1. Подготовка репозитория

Создай GitHub-репозиторий со следующей структурой:

```
crm-auth/
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── requirements.txt
├── frontend/
│   ├── Login.tsx
│   └── ...
└── README.md
```

---

### 2. Развёртывание backend

1. Перейди на [https://render.com](https://render.com)
2. Создай **New Web Service**
3. Выбери репозиторий → `crm-auth`
4. Настройки:
   - **Root Directory**: `backend/`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host=0.0.0.0 --port=10000`
   - **Environment**: Python 3.10

---

### 3. Развёртывание frontend

1. Создай **New Static Site**
2. Root Directory: `frontend/`
3. Build command:
   ```bash
   npm install && npm run build
   ```
4. Publish directory: `dist` или `build` (проверь)

---

### 4. Разрешить CORS в `main.py` (уже готово)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🔑 Авторизация

- `/auth/request-code` — запросить одноразовый код на email
- `/auth/verify` — верификация кода, получение JWT
- React отправляет email и код → получает access_token → сохраняет в `localStorage`

---

## 📩 Примечание

Для отправки реальных email подключи Mailgun или SMTP в `auth.py`