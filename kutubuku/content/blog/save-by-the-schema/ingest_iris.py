import pyspark.sql.types as T

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Defining schema
# fmt: off
iris_schema = T.StructType(
    [
        T.StructField("measurement", T.StructType([
            T.StructField("sepal_length", T.DoubleType()),
            T.StructField("sepal_width", T.DoubleType()),
            T.StructField("petal_length", T.DoubleType()),
            T.StructField("petal_width", T.DoubleType()),
        ])),
        T.StructField("species", T.StringType()),
    ]
)
# fmt: on


# Read with schema
iris = spark.read.json(
    "iris.jsonl", schema=iris_schema, multiLine=False, mode="FAILFAST"
)

iris.show(5)

# Flat the nested schema
iris_df = iris.select("measurement.*", "species")

# Subset the measurement for only petal
# fmt: off
petal_iris_schema = T.StructType(
    [
        T.StructField("measurement", T.StructType([
            T.StructField("petal_length", T.DoubleType()),
            T.StructField("petal_width", T.DoubleType()),
        ])),
        T.StructField("species", T.StringType()),
    ]
)
# fmt: on
petal_iris = spark.read.json(
    "iris.jsonl", schema=petal_iris_schema, multiLine=False, mode="FAILFAST"
)

petal_iris.printSchema()
