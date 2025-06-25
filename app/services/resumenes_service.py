from fastapi import HTTPException
import pandas as pd
from datetime import datetime
from app.db.dynamodb import get_procesos_table


# Obtén la tabla de DynamoDB
table = get_procesos_table()

def get_df_from_dynamo():
    # Escanea toda la tabla y convierte a DataFrame
    response = table.scan()
    items = response.get('Items', [])
    if not items:
        return pd.DataFrame()
    return pd.DataFrame(items)

def resumen_por_llave(llave):
    # Busca el proceso por llave en DynamoDB
    response = table.get_item(Key={"llaveProceso": llave})
    proceso = response.get('Item')
    if not proceso:
        raise HTTPException(status_code=404, detail=f"No se encontró ningún proceso con la llave {llave}")

    hoy = pd.to_datetime(datetime.today().date())
    fecha_proceso = pd.to_datetime(proceso.get('fechaProceso'), errors='coerce')
    fecha_ultima = pd.to_datetime(proceso.get('fechaUltimaActuacion'), errors='coerce')

    antiguedad = (hoy - fecha_proceso).days if pd.notnull(fecha_proceso) else None
    inactividad = (hoy - fecha_ultima).days if pd.notnull(fecha_ultima) else None

    data = {
        'llaveProceso': proceso.get('llaveProceso'),
        'despacho': proceso.get('despacho'),
        'departamento': proceso.get('departamento'),
        'esPrivado': proceso.get('esPrivado'),
        'sujetosProcesales': proceso.get('sujetosProcesales'),
        'fechaProceso': fecha_proceso.date() if pd.notnull(fecha_proceso) else None,
        'fechaUltimaActuacion': fecha_ultima.date() if pd.notnull(fecha_ultima) else None,
        'antiguedad_dias': antiguedad,
        'dias_inactivo': inactividad
    }

    return data

def resumen_por_sujeto(palabra_clave):
    df = get_df_from_dynamo()
    if df.empty or 'sujetosProcesales' not in df.columns:
        raise HTTPException(status_code=404, detail=f"No se encontraron procesos con el sujeto procesal que contenga '{palabra_clave}'")

    filtrado = df[df['sujetosProcesales'].str.contains(palabra_clave, case=False, na=False)]
    if filtrado.empty:
        raise HTTPException(status_code=404, detail=f"No se encontraron procesos con el sujeto procesal que contenga '{palabra_clave}'")

    total_casos = len(filtrado)
    por_despacho = filtrado['despacho'].value_counts().rename_axis('Despacho').reset_index(name='Cantidad')
    por_departamento = filtrado['departamento'].value_counts().rename_axis('Departamento').reset_index(name='Cantidad')
    casos_recientes = filtrado.sort_values('fechaUltimaActuacion', ascending=False).head(20)[
        ['llaveProceso', 'fechaUltimaActuacion', 'despacho', 'departamento']
    ]

    return {
        'total_casos': total_casos,
        'por_despacho': por_despacho.to_dict(orient='records'),
        'por_departamento': por_departamento.to_dict(orient='records'),
        'casos_recientes': casos_recientes.to_dict(orient='records')
    }