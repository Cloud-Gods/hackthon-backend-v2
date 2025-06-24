import httpx
from fastapi import HTTPException

def get_actuaciones_por_id(id_proceso: int):
    url = f"https://ecltkblg39.execute-api.us-east-1.amazonaws.com/ca/actuacionesProceso?idProceso={id_proceso}"
    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Error de conexión: {exc}")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=response.status_code, detail=f"Error HTTP: {exc}")