import great_expectations as ge
from great_expectations.profile.user_configurable_profiler import UserConfigurableProfiler
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
context.create_expectation_suite(expectation_suite_name_1, overwrite_existing=True)
batch1 = ge.dataset.PandasDataset(df1)
profiler1 = UserConfigurableProfiler(batch1)
suite1 = profiler1.build_suite()
context.save_expectation_suite(suite1, expectation_suite_name_1)

# Dataset 2
expectation_suite_name_2 = "dataset2_suite"
context.create_expectation_suite(expectation_suite_name_2, overwrite_existing=True)
batch2 = ge.dataset.PandasDataset(df2)
profiler2 = UserConfigurableProfiler(batch2)
suite2 = profiler2.build_suite()
context.save_expectation_suite(suite2, expectation_suite_name_2)

# Build the data docs
context.build_data_docs()

# Open the data docs in the browser
context.open_data_docs()
