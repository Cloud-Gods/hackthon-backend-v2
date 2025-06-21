from fastapi import APIRouter
from app.api.v1.endpoints import procesos

router = APIRouter()
router.include_router(procesos.router, prefix="/procesos", tags=["procesos"])



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
       {
           "traer": "Trae todos los procesos",
           "endpoint": "/procesos/",
       }
         , {
              "traer": "Trae procesos por nombre",
              "endpoint": "/procesos/by_nombre/{nombre}",
         }, {
              "traer": "Trae procesos por llave de proceso",
              "endpoint": "/procesos/by_llaveProceso/{llaveProceso}",
         }, {
              "traer": "Trae un proceso por ID",
              "endpoint": "/procesos/id_proceso/{id_proceso}",
         }, {
              "traer": "Muestra la versión de la API",
              "endpoint": "/version",
         }
    ]}
