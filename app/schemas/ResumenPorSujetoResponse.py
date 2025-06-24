from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class SujetoResumen(BaseModel):
    total_casos: int
    casos_por_despacho: List[dict]
    casos_por_departamento: List[dict]
    casos_recientes: List[dict]
    procesos_mensuales: List[dict]
    procesos_anuales: List[dict]
    
class SujetoResumenOut(SujetoResumen):
    pass
