# Análisis de viajes de taxi con PySpark y Databricks

Proyecto académico de procesamiento de datos desarrollado con PySpark, Databricks Connect, PyCharm, Git y GitHub.

## Objetivo

Analizar los viajes de taxi disponibles en la tabla de ejemplo:

`samples.nyctaxi.trips`

El proceso calcula las 10 zonas con mayor cantidad de viajes y obtiene:

- Cantidad de viajes.
- Tarifa promedio.
- Distancia promedio.

El resultado se guarda como una tabla Delta en Unity Catalog:

`workspace.default.top_10_zonas_taxi`

## Tecnologías

- Python 3.12
- PySpark
- Databricks Connect
- Databricks Serverless
- Unity Catalog
- PyCharm
- Git
- GitHub

## Estructura del proyecto

```text
databricks-connect-demo/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── transformations.py
├── notebooks/
├── data/
├── tests/
├── docs/
├── resources/
├── requirements.txt
├── README.md
└── .gitignore
```

## Flujo del proyecto

```text
PyCharm
   ↓
Databricks Connect
   ↓
PySpark en Databricks Serverless
   ↓
Lectura de samples.nyctaxi.trips
   ↓
Transformación y agregación
   ↓
Tabla Delta en Unity Catalog
   ↓
Código versionado en GitHub
```

## Configuración

Crear un entorno virtual con Python 3.12:

```bash
python3.12 -m venv .venv
```

Instalar las dependencias:

```bash
./.venv/bin/python -m pip install -r requirements.txt
```

La autenticación con Databricks debe configurarse localmente mediante Databricks CLI usando el perfil `DEFAULT`.

## Ejecución

Desde la raíz del proyecto:

```bash
./.venv/bin/python -m src.main
```

## Tabla de origen

```text
samples.nyctaxi.trips
```

## Tabla de resultado

```text
workspace.default.top_10_zonas_taxi
```

## Resultado esperado

El programa muestra las 10 zonas de recogida con más viajes y guarda el resultado permanentemente como una tabla Delta administrada en Databricks.

## Repositorio

```text
https://github.com/AJoelSS/DataBricks
```