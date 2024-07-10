from pyspark.sql import SparkSession

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
catalyst_plan = df._jdf.queryExecution().logical()
size_bytes = spark._jsparkSession.sessionState().executePlan(catalyst_plan).optimizedPlan().stats().sizeInBytes()

# Unpersist the DataFrame
df.unpersist()

# Print the total table size
print("Total table size:", convert_size_bytes(size_bytes))

# Stop the Spark session
spark.stop()
