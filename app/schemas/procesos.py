from pydantic import BaseModel, EmailStr
from typing import List, Optional
class CantFila(BaseModel):
    nombre: str
    documentoUsuario: str
    rol: str


class ProcesosCreate(BaseModel):
    idConexion: int
    esPrivado: bool
    departamento: str
    llaveProceso: str
    idProceso: int
    fechaUltimaActuacion: str
    cantFilas: List[CantFila]
    sujetosProcesales: str
    despacho: str
    fechaProceso: str
class ProcesosOut(ProcesosCreate):
    pass
