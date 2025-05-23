from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/items", tags=["items"])

class Item(BaseModel):
    id: str | None = None
    nombre: str
    precio: float
    descripcion: str | None = None
    disponibilidad: bool

items_db: List[Item] = []

@router.post("/", response_model=Item)
def crear_item(item: Item):
    item.id = str(uuid4())
    items_db.append(item)
    return item

@router.get("/", response_model=List[Item])
def obtener_items():
    return items_db

@router.get("/{item_id}", response_model=Item)
def obtener_item_por_id(item_id: str):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")
