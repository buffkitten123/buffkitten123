import pandas as pd

# Sample DataFrames with additional columns and duplicate indices
df1 = pd.DataFrame({
    'A': [1, 1, 2, 2, 3, 3],
    'B': [1, 2, 3, 4, 5, 6],
    'C': ['x', 'y', 'z', 'a', 'b', 'c']  # Additional column
})

df2 = pd.DataFrame({
    'A': [1, 1, 2, 2, 3, 3, 4],
    'B': [1, 2, 3, 5, 5, 6, 7],  # Note the differences at (2, 5) and extra key (4, 7)
    'C': ['x', 'y', 'z', 'a', 'b', 'd']  # Additional column
})

# Select only the columns of interest
df1_subset = df1[['A', 'B']]
df2_subset = df2[['A', 'B']]

# Merge the DataFrames on 'A' to align rows and compare
merged_df = df1_subset.merge(df2_subset, on='A', how='outer', suffixes=('_df1', '_df2'))

# Identify rows with differing 'B' values
differing_rows = merged_df[merged_df['B_df1'] != merged_df['B_df2']]

# Remove rows with NaN values in 'B_df1' and 'B_df2'
differing_rows_cleaned = differing_rows.dropna(subset=['B_df1', 'B_df2'])

# Get a DataFrame with unique values in column 'A'
unique_differing_rows_cleaned = differing_rows_cleaned.drop_duplicates(subset='A')

print("Unique keys with differing values:")
print(unique_differing_rows_cleaned)
