from app.schemas.procesos import ProcesosCreate
from app.db.dynamodb import get_procesos_table
from botocore.exceptions import ClientError
from datetime import datetime


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

def get_resumen_por_llave(llave):
    table = get_procesos_table()
    try:
        response = table.scan(
            FilterExpression="llaveProceso = :llave",
            ExpressionAttributeValues={":llave": llave}
        )
        items = response.get("Items", [])
        if not items:
            return None

        proceso = items[0]
        hoy = datetime.today().date()

        fecha_proceso = proceso.get('fechaProceso')
        fecha_ultima = proceso.get('fechaUltimaActuacion')

        # Parse fechas
        try:
            fecha_proceso_dt = datetime.strptime(fecha_proceso, "%Y-%m-%d").date() if fecha_proceso else None
        except Exception:
            fecha_proceso_dt = None
        try:
            fecha_ultima_dt = datetime.strptime(fecha_ultima, "%Y-%m-%d").date() if fecha_ultima else None
        except Exception:
            fecha_ultima_dt = None

        antiguedad = (hoy - fecha_proceso_dt).days if fecha_proceso_dt else None
        inactividad = (hoy - fecha_ultima_dt).days if fecha_ultima_dt else None

        data = {
            'llaveProceso': proceso.get('llaveProceso'),
            'despacho': proceso.get('despacho'),
            'departamento': proceso.get('departamento'),
            'esPrivado': proceso.get('esPrivado'),
            'sujetosProcesales': proceso.get('sujetosProcesales'),
            'fechaProceso': str(fecha_proceso_dt) if fecha_proceso_dt else None,
            'fechaUltimaActuacion': str(fecha_ultima_dt) if fecha_ultima_dt else None,
            'antiguedad_dias': antiguedad,
            'dias_inactivo': inactividad
        }
        return data
    except ClientError as e:
        raise Exception(f"Error al obtener proceso: {e.response['Error']['Message']}")

def get_resumen_por_sujeto(nombre_razon):
    table = get_procesos_table()
    try:
        response = table.scan()
        items = response.get("Items", [])
        filtrado = [item for item in items if nombre_razon.lower() in item.get('sujetosProcesales', '').lower()]
        if not filtrado:
            return None

        total_casos = len(filtrado)
        # Conteo por despacho y departamento
        despachos = {}
        departamentos = {}
        casos_recientes = sorted(
            filtrado,
            key=lambda x: x.get('fechaUltimaActuacion', ''),
            reverse=True
        )[:5]

        for item in filtrado:
            despachos[item.get('despacho', '')] = despachos.get(item.get('despacho', ''), 0) + 1
            departamentos[item.get('departamento', '')] = departamentos.get(item.get('departamento', ''), 0) + 1

        # Top 10
        top_despachos = dict(sorted(despachos.items(), key=lambda x: x[1], reverse=True)[:10])
        top_departamentos = dict(sorted(departamentos.items(), key=lambda x: x[1], reverse=True)[:10])

        casos_recientes_out = [
            {
                "llaveProceso": c.get("llaveProceso"),
                "fechaUltimaActuacion": c.get("fechaUltimaActuacion"),
                "despacho": c.get("despacho"),
                "departamento": c.get("departamento")
            }
            for c in casos_recientes
        ]

        return {
            "total_casos": total_casos,
            "por_despacho": top_despachos,
            "por_departamento": top_departamentos,
            "casos_recientes": casos_recientes_out
        }
    except ClientError as e:
        raise Exception(f"Error al obtener procesos por sujeto: {e.response['Error']['Message']}")