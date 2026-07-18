from databricks.connect import DatabricksSession

from src.transformations import obtener_top_zonas


TABLA_ORIGEN = "samples.nyctaxi.trips"
TABLA_DESTINO = "workspace.default.top_10_zonas_taxi"


def main() -> None:
    spark = (
        DatabricksSession.builder
        .serverless()
        .profile("DEFAULT")
        .getOrCreate()
    )

    trips = spark.read.table(TABLA_ORIGEN)
    resultado = obtener_top_zonas(trips, limite=10)

    print("TOP 10 ZONAS CON MÁS VIAJES")
    resultado.show(truncate=False)

    (
        resultado.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(TABLA_DESTINO)
    )

    print(f"Tabla guardada correctamente: {TABLA_DESTINO}")


if __name__ == "__main__":
    main()