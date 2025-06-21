from fastapi import APIRouter, HTTPException
from app.schemas.procesos import ProcesosOut
from app.services import procesos_service

router = APIRouter()

@router.get("/", response_model=list[ProcesosOut])
def read_all():
    procesos = procesos_service.get_procesos()
    if not procesos:
        raise HTTPException(status_code=404, detail="No se encontraron procesos")
    return procesos

@router.get("/by_nombre/{nombre}", response_model=list[ProcesosOut])
def read_by_nombre(nombre: str):
    procesos = procesos_service.get_procesos_by_nombre(nombre)
    if not procesos:
        raise HTTPException(status_code=404, detail="No se encontraron procesos con ese nombre")
    return procesos

@router.get("/by_llaveProceso/{llaveProceso}", response_model=list[ProcesosOut])
def read_by_llaveProceso(llaveProceso: str):
    procesos = procesos_service.get_procesos_by_llaveProceso(llaveProceso)
    if not procesos:
        raise HTTPException(status_code=404, detail="No se encontraron procesos con esa llave de proceso")
    return procesos

@router.get("/id_proceso/{id_proceso}", response_model=ProcesosOut)
def read_by_id(id_proceso: str):
    proceso = procesos_service.get_proceso_by_id(id_proceso)
    if not proceso:
        raise HTTPException(status_code=404, detail="Proceso no encontrado")
    return proceso

@router.post("/", response_model=ProcesosOut)
def show_version():
    return procesos_service.show_version()  

