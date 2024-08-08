import pandas as pd

# Sample DataFrames with additional columns
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

# Set 'A' as the index for both DataFrames
df1_subset.set_index('A', inplace=True)
df2_subset.set_index('A', inplace=True)

# Reindex both DataFrames to ensure all keys are considered
df1_subset = df1_subset.reindex(df1_subset.index.union(df2_subset.index))
df2_subset = df2_subset.reindex(df1_subset.index)

# Compare DataFrames
comparison = df1_subset.compare(df2_subset)

# Get the keys (index) with differing values
differing_keys = comparison.index.tolist()

print("Keys with differing values:", differing_keys)
