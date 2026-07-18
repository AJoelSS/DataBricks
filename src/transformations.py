from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def obtener_top_zonas(trips: DataFrame, limite: int = 10) -> DataFrame:
    """Genera el ranking de zonas con mayor cantidad de viajes."""

    return (
        trips
        .filter(
            (F.col("fare_amount") > 0)
            & (F.col("trip_distance") > 0)
            & F.col("pickup_zip").isNotNull()
        )
        .groupBy("pickup_zip")
        .agg(
            F.count("*").alias("cantidad_viajes"),
            F.round(F.avg("fare_amount"), 2).alias("tarifa_promedio"),
            F.round(F.avg("trip_distance"), 2).alias("distancia_promedio"),
        )
        .orderBy(F.desc("cantidad_viajes"))
        .limit(limite)
    )