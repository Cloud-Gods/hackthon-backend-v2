from fastapi import APIRouter, HTTPException
from app.services.procesos_service import get_resumen_por_llave, get_resumen_por_sujeto

router = APIRouter()

@router.get("/proceso/{llave}")
def resumen_por_llave(llave: str):
    data = get_resumen_por_llave(llave)
    if not data:
        raise HTTPException(status_code=404, detail=f"No se encontró ningún proceso con la llave {llave}")
    return data

@router.get("/sujeto/{nombre_razon}")
def resumen_por_sujeto(nombre_razon: str):
    data = get_resumen_por_sujeto(nombre_razon)
    if not data:
        raise HTTPException(status_code=404, detail=f"No se encontraron procesos con el sujeto procesal '{nombre_razon}'")
    return data