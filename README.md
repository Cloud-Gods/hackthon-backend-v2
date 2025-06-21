# Proyecto FastAPI

Este proyecto es una aplicación web construida con FastAPI. A continuación se detallan las instrucciones para configurar y ejecutar el proyecto.

## Estructura del Proyecto

```
proyecto
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   └── v1
│   │       └── endpoints
│   │           └── procesos.py
│   ├── schemas
│   │   └── procesos.py
│   └── services
│       └── procesos_service.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.7 o superior
- Docker (opcional, para ejecutar en contenedor)

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd proyecto
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar la aplicación localmente, utiliza el siguiente comando:

```
uvicorn app.main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

## Docker

Para construir y ejecutar la aplicación en un contenedor Docker, utiliza los siguientes comandos:

1. Construir la imagen:
   ```
   docker build -t nombre_de_la_imagen .
   ```

2. Ejecutar el contenedor:
   ```
   docker run -d -p 8000:8000 nombre_de_la_imagen
   ```

La aplicación estará disponible en `http://localhost:8000`.

## Documentación de la API

La documentación interactiva de la API está disponible en `http://localhost:8000/docs`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.