import pyspark.sql.functions as F
from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()

lab_equipment = spark.createDataFrame(
    [
        [1, "Microscope"],
        [2, "Centrifuge"],
        [3, "Pipette"],
        [4, "Water bath"],
        [5, "Spectrometer"],
    ],
    ["equipment_id", "equipment_name"],
)

lab_protocol = spark.createDataFrame(
    [
        [101, "Protocol A", 1],
        [101, "Protocol A", 2],
        [102, "Protocol B", 3],
        [102, "Protocol B", 6],
        [103, "Protocol C", 5],
        [104, "Protocol D", 1],
        [104, "Protocol D", 2],
        [104, "Protocol D", 5],
    ],
    ["protocol_id", "protocol_name", "equipment_id"],
)

# INNER JOIN: collect protocol with the corresponding equipments
(
    lab_protocol.join(lab_equipment, on=["equipment_id"], how="inner")
    .groupBy("protocol_name")
    .agg(F.collect_list("equipment_name").alias("equipments"))
    .orderBy("protocol_name")
    .show(truncate=False)
)

# LEFT JOIN: ensure that missing equipments are shown
(
    lab_protocol.join(lab_equipment, on=["equipment_id"], how="left")
    # Replace `null` with a value MISSING
    .withColumn(
        "equipment",
        F.when(F.col("equipment_name").isNull(), F.lit("MISSING")).otherwise(
            F.col("equipment_name")
        ),
    )
    .groupBy("protocol_name")
    .agg(F.collect_list("equipment").alias("equipments"))
    .orderBy("protocol_name")
    .show(truncate=False)
)

# LEFT_SEMI: to find lab equipment that is at least used once by a lab protocol
(lab_equipment.join(lab_protocol, on=["equipment_id"], how="left_semi").show())


# LEFT_ANTO: to find lab equipment that is NOT at least used once by a lab protocol
(lab_equipment.join(lab_protocol, on=["equipment_id"], how="left_anti").show())
