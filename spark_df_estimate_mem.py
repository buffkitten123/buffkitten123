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

# Function to estimate the size of the DataFrame
def estimate_dataframe_size(df):
    try:
        # Get a sample of the DataFrame
        sample_fraction = 0.1
        sample = df.sample(False, sample_fraction).rdd.map(lambda row: len(str(row)))

        # Calculate the average size of a row in the sample
        average_row_size = sample.mean()

        # Estimate the total size
        total_rows = df.count()
        estimated_size = total_rows * average_row_size
        
        return estimated_size
    except Exception as e:
        print(f"An error occurred while estimating DataFrame size: {e}")
        return None

# Estimate the size of the DataFrame
estimated_size_bytes = estimate_dataframe_size(df)

# Unpersist the DataFrame
df.unpersist()

# Print the total table size
if estimated_size_bytes is not None:
    print("Estimated total table size:", convert_size_bytes(estimated_size_bytes))
else:
    print("Could not determine the size of the DataFrame.")
