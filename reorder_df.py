def reorder_columns(df):
    # Identify columns with '_apple' in their names
    apple_cols = [col for col in df.columns if '_apple' in col]
    
    # Identify non-apple columns
    non_apple_cols = [col for col in df.columns if '_apple' not in col]
    
    # Determine the number of '_apple' columns
    num_apples = len(apple_cols)
    
    # Reorder columns between the first column and the apple columns
    reorder_non_apple_cols = non_apple_cols[1:-num_apples]  # exclude the first column and the last num_apples columns
    reordered_cols = [non_apple_cols[0]]  # start with the first column
    
    i = 0
    while i < len(reorder_non_apple_cols):
        reordered_cols.append(reorder_non_apple_cols[i])
        if i + 2 < len(reorder_non_apple_cols):
            reordered_cols.append(reorder_non_apple_cols[i + 2])
        i += 1
    
    reordered_cols = reordered_cols[:len(reorder_non_apple_cols)] + non_apple_cols[-num_apples:] + apple_cols
    
    # Create the new reordered DataFrame
    final_df = df[reordered_cols]
    
    return final_df
