# Extract and print detailed results
def print_detailed_results(results):
    for result in results['results']:
        expectation_type = result['expectation_config']['expectation_type']
        column_name = result['expectation_config']['kwargs']['column']
        success = result['success']
        unexpected_count = result['result']['unexpected_count']
        unexpected_list = result['result']['unexpected_list']

        print(f"Expectation: {expectation_type}")
        print(f"Column: {column_name}")
        print(f"Success: {success}")
        print(f"Unexpected Count: {unexpected_count}")

        if not success:
            print("Non-unique values found:")
            for value in unexpected_list:
                print(f" - {value}")
        print("-" * 20)

# Print the detailed results
print_detailed_results(results)
