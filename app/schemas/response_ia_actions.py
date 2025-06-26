# schemas/response_actions.py
from pydantic import BaseModel
from typing import Literal

class ResponseActionsIAType(BaseModel):
    actuacion: int
    clasificacion: Literal['Alta', 'Media', 'Baja', 'Nula']
    resumen: str