# Extract all mismatched rows
def get_all_mismatched_rows(compare):
    mismatch_df = compare.all_mismatch()
    mismatched_columns = [col for col in compare.df1.columns if col != 'acct_id']
    
    mismatch_details = []
    for idx, row in mismatch_df.iterrows():
        mismatch_row = {'acct_id': row['acct_id']}
        for col in mismatched_columns:
            df1_val = row[f'{col}_df1']
            df2_val = row[f'{col}_df2']
            if df1_val != df2_val:
                mismatch_row[f'{col}_df1'] = df1_val
                mismatch_row[f'{col}_df2'] = df2_val
        mismatch_details.append(mismatch_row)
    
    return pd.DataFrame(mismatch_details)

# Get all mismatched rows
all_mismatched_rows = get_all_mismatched_rows(compare)

# Function to clean and format the report
import re
def clean_report(report):
    # Replace newline characters with a space
    report = report.replace('\n', ' ')
    
    # Replace multiple spaces with a single space
    report = re.sub(r'\s+', ' ', report).strip()
    
    return report

# Clean the report
cleaned_report = clean_report(report)

# Print the cleaned report
print("Cleaned Report:\n", cleaned_report)

# Print all mismatched rows
print("\nAll Mismatched Rows with Details:\n", all_mismatched_rows)
