
from fastapi import APIRouter, HTTPException
from app.services.actuaciones_service import get_actuaciones_por_id
from app.schemas.response_ia_actions import ResponseActionsIAType
from app.services.ia_service import ConexionIA
import json
from typing import List
#importar JsonResponse
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/acciones_ia/{id_proceso}", response_model=List[ResponseActionsIAType])
def procesar_acciones_ia(id_proceso: int):
    actuaciones = get_actuaciones_por_id(id_proceso)

    if not actuaciones:
        raise HTTPException(status_code=404, detail="No se encontraron actuaciones.")

    conexion_ia = ConexionIA()
    resultado_json_str = conexion_ia.clasificar_actuacionesList(actuaciones)

    try:
        if isinstance(resultado_json_str, str):
            print(f"Respuesta de IA: {resultado_json_str}")
            return json.loads(resultado_json_str)
        return resultado_json_str
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Error al parsear respuesta de IA: {e}")
    
        