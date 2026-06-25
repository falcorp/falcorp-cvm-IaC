import sys
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession

args = getResolvedOptions(sys.argv, ["SOURCE_PATH", "TARGET_PATH"])

spark = SparkSession.builder.appName("subscribers-etl").getOrCreate()

df = spark.read.option("header", "true").csv(args["SOURCE_PATH"])

df_clean = df.dropDuplicates(["customer_id"])

df_clean.write.mode("overwrite").parquet(args["TARGET_PATH"])
