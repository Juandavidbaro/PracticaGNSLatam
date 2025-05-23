from fastapi import FastAPI
from routes import items 

app = FastAPI(title="API de Items")

app.include_router(items.router)
