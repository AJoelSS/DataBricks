from databricks.connect import DatabricksSession


spark = (
    DatabricksSession.builder
    .serverless()
    .profile("DEFAULT")
    .getOrCreate()
)

spark.range(3).show()