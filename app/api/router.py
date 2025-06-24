from fastapi import APIRouter
from app.api.v1.endpoints import procesos , resumenes, actuaciones

router = APIRouter()
router.include_router(procesos.router, prefix="/procesos", tags=["procesos"])
router.include_router(resumenes.router, prefix="/resumenes", tags=["resumenes"])
router.include_router(actuaciones.router, prefix="/actuaciones", tags=["actuaciones"])

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
         },
          {
                "traer": "Resumen por llave de proceso",
                "endpoint": "/resumenes/resumen/llave/{llave}",
          }, 
           
          {
               "traer": "Resumen por sujeto procesal",
               "endpoint": "/resumenes/resumen/sujeto/{palabra_clave}",
          }, 
          {
               "traer": "Actuaciones por ID de proceso",
               "endpoint": "/actuaciones/actuaciones/{id_proceso}",
          }
    ]}
