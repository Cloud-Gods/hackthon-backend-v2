from fastapi import APIRouter, HTTPException
from app.services.resumenes_service import resumen_por_llave, resumen_por_sujeto
from typing import Optional, Dict, Any
from app.schemas.ProcesoResumen import ResumenPorLlaveOut
from app.schemas.ResumenPorSujetoResponse import SujetoResumenOut

router = APIRouter()


@router.get("/resumen/llave/{llave}", response_model=ResumenPorLlaveOut)
async def get_resumen_por_llave(llave: str):
    resultado = resumen_por_llave(llave)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    return resultado.to_dict(orient='records')[0]

@router.get("/resumen/sujeto/{palabra_clave}", response_model=SujetoResumenOut)
async def get_resumen_por_sujeto(palabra_clave: str):
    resultado = resumen_por_sujeto(palabra_clave)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Sujeto procesal no encontrado")
    return resultado