def rearrange_columns(df, ending_match):
    # Count the number of columns ending with the specified match
    matched_columns = [col for col in df.columns if col.endswith(ending_match)]
    match_count = len(matched_columns)

    # Define the number of rearranged columns
    rearranged_columns_count = match_count * 2

    # Identify the columns to be rearranged (excluding col1 and the last matched columns)
    initial_columns = [col for col in df.columns if not col.endswith(ending_match)]
    columns_to_rearrange = initial_columns[1:rearranged_columns_count+1]

    # Create the new column order
    new_order = ['col1']
    for i in range(rearranged_columns_count // 2):
        new_order.append(columns_to_rearrange[i])
        new_order.append(columns_to_rearrange[i + rearranged_columns_count // 2])
    new_order += initial_columns[rearranged_columns_count+1:] + matched_columns

    # Rearrange the DataFrame
    df_rearranged = df[new_order]
    return df_rearranged
