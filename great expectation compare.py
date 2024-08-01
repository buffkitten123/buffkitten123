import great_expectations as ge
from great_expectations.profile.basic_dataset_profiler import BasicDatasetProfiler

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
df1 = ge.from_pandas(pd.DataFrame(data1))
df2 = ge.from_pandas(pd.DataFrame(data2))

# Initialize a DataContext
context = ge.data_context.DataContext()

# Dataset 1
expectation_suite_name_1 = "dataset1_suite"
suite1 = context.create_expectation_suite(expectation_suite_name_1, overwrite_existing=True)
df1.set_default_expectation_suite(suite1)
results1 = BasicDatasetProfiler.profile(df1)
context.save_expectation_suite(results1["expectation_suite"], expectation_suite_name_1)

# Dataset 2
expectation_suite_name_2 = "dataset2_suite"
suite2 = context.create_expectation_suite(expectation_suite_name_2, overwrite_existing=True)
df2.set_default_expectation_suite(suite2)
results2 = BasicDatasetProfiler.profile(df2)
context.save_expectation_suite(results2["expectation_suite"], expectation_suite_name_2)

# Build the data docs
context.build_data_docs()

# Open the data docs in the browser
context.open_data_docs()
