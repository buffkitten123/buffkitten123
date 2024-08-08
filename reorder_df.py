def reorder_dataframe(df):
    # Identify columns with '_apple' in their names
    apple_cols = [col for col in df.columns if '_apple' in col]
    
    # Count the number of '_apple' columns
    num_apples = len(apple_cols)
    
    # Determine how many rows to keep unchanged
    rows_to_keep = num_apples
    
    # Split the DataFrame into two parts: rows to reorder and rows to keep
    df_to_reorder = df.iloc[:-rows_to_keep]
    df_to_keep = df.iloc[-rows_to_keep:]
    
    # Perform the reordering of the rows to reorder
    reordered_index = []
    i = 0
    while i < len(df_to_reorder):
        reordered_index.extend([i, i+2])
        i += 1
    reordered_index = reordered_index[:len(df_to_reorder)]
    
    # Create the new reordered DataFrame
    df_reordered = df_to_reorder.iloc[reordered_index].reset_index(drop=True)
    
    # Concatenate the reordered DataFrame with the rows to keep
    final_df = pd.concat([df_reordered, df_to_keep]).reset_index(drop=True)
    
    return final_df
