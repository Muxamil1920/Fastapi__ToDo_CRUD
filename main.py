from fastapi import FastAPI, status
from .models import Base
from .database import engine
from TodosApp.routers import auth, todos, admin, user


app = FastAPI()

@app.get("/health",status_code=status.HTTP_200_OK)
async def check_health():
    return {'status': 'Healthy'}

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)
