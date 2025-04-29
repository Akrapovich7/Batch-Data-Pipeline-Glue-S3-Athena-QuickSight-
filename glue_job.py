import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_timestamp
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize context
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# === 1. Load CSV from S3 raw folder ===
input_path = "s3://batch-data-pipeline-bucket-v1/raw/online_course_engagement.csv"
df = spark.read.option("header", "true").csv(input_path)

# === 2. Transform data ===
df = df.withColumn("event_timestamp", to_timestamp("event_timestamp", "yyyy-MM-dd HH:mm:ss"))
df = df.withColumn("duration_minutes", col("duration_minutes").cast("int"))

# Example filter: remove 0-duration events
df = df.filter(col("duration_minutes") > 0)

# === 3. Write to S3 in Parquet format ===
output_path = "s3://batch-data-pipeline-bucket-v1/processed/online_course_engagement/"
df.write.mode("overwrite").parquet(output_path)

job.commit()
