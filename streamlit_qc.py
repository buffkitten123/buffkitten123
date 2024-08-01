import streamlit as st
import pandas as pd

# Example DataFrames
data1 = {'id': [1, 2, 3, 4], 'name': ['John Doe', 'Jane Smith', 'Jake Johnson', 'John Doe'], 'address': ['123 Elm St', '456 Oak St', '789 Pine St', '123 Elm St']}
data2 = {'id': [4, 5, 6, 8], 'name': ['John Doe', 'J. Smith', 'Jacob Johnson', 'Jon Doe'], 'address': ['123 Elm Street', '456 Oak Street', '789 Pine Street', '123 Elm Street']}
data3 = {'id': [7, 8, 9], 'name': ['John Doe', 'Jane Smith', 'Jacob Johnson'], 'address': ['123 Elm St', '456 Oak St', '789 Pine Street']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Streamlit App
st.title("Interactive DataFrame Comparison")

# Display DataFrames
st.header("DataFrame 1")
st.dataframe(df1)

st.header("DataFrame 2")
st.dataframe(df2)

st.header("DataFrame 3")
st.dataframe(df3)

# Select a row from DataFrame 1
st.header("Select a row from DataFrame 1")
selected_row = st.selectbox("Select row by 'name'", df1['name'].unique())

if selected_row:
    st.write(f"Selected: {selected_row}")

    # Filter DataFrames by selected row
    filtered_df2 = df2[df2['name'].str.contains(selected_row, case=False, na=False)]
    filtered_df3 = df3[df3['name'].str.contains(selected_row, case=False, na=False)]

    st.header("Matching Rows in DataFrame 2")
    if not filtered_df2.empty:
        st.dataframe(filtered_df2)
    else:
        st.write("No matching rows found in DataFrame 2.")

    st.header("Matching Rows in DataFrame 3")
    if not filtered_df3.empty:
        st.dataframe(filtered_df3)
    else:
        st.write("No matching rows found in DataFrame 3.")
