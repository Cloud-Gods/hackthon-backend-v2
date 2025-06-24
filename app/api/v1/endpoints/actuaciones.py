from fastapi import APIRouter
from app.services.actuaciones_service import get_actuaciones_por_id

router = APIRouter()

@router.get("/actuaciones/{id_proceso}")
def actuaciones(id_proceso: int):
    return get_actuaciones_por_id(id_proceso)