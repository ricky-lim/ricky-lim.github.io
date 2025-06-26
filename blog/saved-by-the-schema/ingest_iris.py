import pyspark.sql.types as T
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.getOrCreate()

# --- Define the full Iris schema ---
# fmt: off
iris_schema = T.StructType([
    T.StructField("measurement", T.StructType([
        T.StructField("sepal_length", T.DoubleType()),
        T.StructField("sepal_width", T.DoubleType()),
        T.StructField("petal_length", T.DoubleType()),
        T.StructField("petal_width", T.DoubleType()),
    ])),
    T.StructField("species", T.StringType()),
])
# fmt: on

# --- Read the Iris dataset with schema enforcement ---
iris = spark.read.json(
    "iris.jsonl", schema=iris_schema, multiLine=False, mode="FAILFAST"
)

# Show the first 5 rows
iris.show(5)

# --- Flatten the nested measurement fields ---
iris_df = iris.select("measurement.*", "species")

# --- Define a schema for only petal measurements ---
# fmt: off
petal_iris_schema = T.StructType([
    T.StructField("measurement", T.StructType([
        T.StructField("petal_length", T.DoubleType()),
        T.StructField("petal_width", T.DoubleType()),
    ])),
    T.StructField("species", T.StringType()),
])
# fmt: on

# --- Read only petal measurements and species ---
petal_iris = spark.read.json(
    "iris.jsonl", schema=petal_iris_schema, multiLine=False, mode="FAILFAST"
)

# Print the resulting schema
petal_iris.printSchema()
