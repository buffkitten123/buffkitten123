from pyspark.sql import SparkSession
import math

def convert_size_bytes(size_bytes):
    """Convert bytes to a human-readable format."""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

# Initialize Spark session
spark = SparkSession.builder \
    .appName("DataFrameSizeCalculator") \
    .getOrCreate()

# Example DataFrame
data = [(1, "foo"), (2, "bar"), (3, "baz")]
df = spark.createDataFrame(data, ["id", "value"])

# Cache the DataFrame
df.cache()
df.count()  # Force caching

# Access hidden parameters to get DataFrame size in bytes
try:
    catalyst_plan = df._jdf.queryExecution().logical()
    session_state = spark._jsparkSession.sessionState()
    executed_plan = session_state.executePlan(catalyst_plan)
    size_bytes = executed_plan.optimizedPlan().stats().sizeInBytes()
except Exception as e:
    size_bytes = None
    print(f"An error occurred while accessing DataFrame size: {e}")

# Unpersist the DataFrame
df.unpersist()

# Print the total table size
if size_bytes is not None:
    print("Total table size:", convert_size_bytes(size_bytes))
else:
    print("Could not determine the size of the DataFrame.")
