from fastapi import APIRouter
from app.api.v1.endpoints import procesos , resumenes, actuaciones, ia_route

router = APIRouter()
router.include_router(procesos.router, prefix="/procesos", tags=["procesos"])
router.include_router(resumenes.router, prefix="/resumenes", tags=["resumenes"])
router.include_router(actuaciones.router, prefix="/actuaciones", tags=["actuaciones"])
router.include_router(ia_route.router, prefix="/ia", tags=["ia"])

@router.get("/version") 
def show_version():
    from app.services import procesos_service
    return procesos_service.show_version()

@router.get("/")
def root():
    return {"message": "Welcome to the Procesos API. Use /procesos for endpoints."}


@router.get("/docs")
def docs():
    return {"message": [
          {"url": "/procesos", "description": "Endpoints relacionados con procesos"},
          {"url": "/resumenes", "description": "Endpoints relacionados con resúmenes de procesos"},
          {"url": "/actuaciones", "description": "Endpoints relacionados con actuaciones de procesos"},
          {"url": "/version", "description": "Obtener la versión de la API"},
          {"url": "/ia", "description": "Procesar acciones de IA para un proceso específico"},
    ]}
