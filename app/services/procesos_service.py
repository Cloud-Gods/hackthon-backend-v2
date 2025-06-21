from app.schemas.procesos import ProcesosCreate
from app.db.dynamodb import get_procesos_table
from botocore.exceptions import ClientError


def get_procesos():
    table = get_procesos_table()
    try:
        response = table.scan()
        return response.get("Items", [])
    except ClientError as e:
        raise Exception(f"Error al obtener procesos: {e.response['Error']['Message']}")
    
def get_proceso_by_id(id_proceso: str):
    table = get_procesos_table()
    try:
        # Convertir a int si el campo es numérico en DynamoDB
        response = table.get_item(Key={"idProceso": int(id_proceso)})
        return response.get("Item")
    except ClientError as e:
        raise Exception(f"Error al obtener usuario: {e.response['Error']['Message']}")
        
def get_procesos_by_nombre(nombre: str):
    table = get_procesos_table()
    try:
        response = table.scan()
        items = response.get("Items", [])
        # Filtrar en Python: buscar nombre dentro de cada cantFilas
        resultados = []
        for item in items:
            for fila in item.get("cantFilas", []):
                if fila.get("nombre", "").lower() == nombre.lower():
                    resultados.append(item)
                    break  # Si ya lo encontró en una fila, no revisa las demás
        return resultados
    except ClientError as e:
        raise Exception(f"Error al obtener procesos por nombre: {e.response['Error']['Message']}")
    
def get_procesos_by_llaveProceso(llaveProceso: str):
    table = get_procesos_table()
    try:
        response = table.scan(
            FilterExpression="contains(llaveProceso, :llaveProceso)",
            ExpressionAttributeValues={":llaveProceso": llaveProceso}
        )
        return response.get("Items", [])
    except ClientError as e:
        raise Exception(f"Error al obtener procesos por llaveProceso: {e.response['Error']['Message']}")
    
def show_version():
    return "Version 1.0.0"