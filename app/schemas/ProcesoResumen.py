from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class ResumenPorLlaveResponse(BaseModel):
    llaveProceso: str
    despacho: str
    departamento: str
    esPrivado: bool
    sujetosProcesales: str
    fechaProceso: Optional[str]
    fechaUltimaActuacion: Optional[str]
    antiguedad_dias: Optional[int]
    dias_inactivo: Optional[int]
class  ResumenPorLlaveOut(ResumenPorLlaveResponse):
    pass