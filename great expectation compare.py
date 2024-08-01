import great_expectations as ge
import pandas as pd

# Sample data
data1 = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
data2 = {
    'A': [5, 6, 7, 8, 9],
    'B': [50, 60, 70, 80, 90]
}

# Create pandas DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Initialize a DataContext
context = ge.data_context.DataContext()

# Dataset 1
expectation_suite_name_1 = "dataset1_suite"
context.add_or_update_expectation_suite(expectation_suite_name_1)
batch_kwargs_1 = {
    "datasource": "pandas", 
    "dataset": df1
}
batch_1 = context.get_batch(batch_kwargs=batch_kwargs_1, expectation_suite_name=expectation_suite_name_1)
batch_1.profile(UserConfigurableProfiler, profiler_configuration="basic")
context.save_expectation_suite(batch_1.get_expectation_suite(), expectation_suite_name_1)

# Dataset 2
expectation_suite_name_2 = "dataset2_suite"
context.add_or_update_expectation_suite(expectation_suite_name_2)
batch_kwargs_2 = {
    "datasource": "pandas", 
    "dataset": df2
}
batch_2 = context.get_batch(batch_kwargs=batch_kwargs_2, expectation_suite_name=expectation_suite_name_2)
batch_2.profile(UserConfigurableProfiler, profiler_configuration="basic")
context.save_expectation_suite(batch_2.get_expectation_suite(), expectation_suite_name_2)

# Build the data docs
context.build_data_docs()

# Open the data docs in the browser
context.open_data_docs()
