import streamlit as st
import pandas as pd
from io import StringIO

st.title("Splitwise Bank App")
st.write("Upload your credit and debit card CSV files to process transactions")

# Credit Card Files Section
st.header("Credit Card Files")
credit_files = st.file_uploader(
    "Upload Credit Card CSV files",
    type=['csv'],
    accept_multiple_files=True,
    key='credit'
)

# Debit Card Files Section
st.header("Debit Card Files")
debit_files = st.file_uploader(
    "Upload Debit Card CSV files",
    type=['csv'],
    accept_multiple_files=True,
    key='debit'
)

# Process Credit Card Files
if credit_files:
    st.subheader("Credit Card Files Processing")
    
    combined_credit_df = pd.DataFrame()
    
    for i, file in enumerate(credit_files):
        st.write(f"Processing: {file.name}")
        df = pd.read_csv(file)
        st.write(f"  - Rows: {len(df)}, Columns: {len(df.columns)}")
        
        # Combine all credit card files
        if combined_credit_df.empty:
            combined_credit_df = df
        else:
            combined_credit_df = pd.concat([combined_credit_df, df], ignore_index=True)
    
    st.success(f"Combined {len(credit_files)} credit card file(s) into one file")
    st.write(f"Total rows in combined credit file: {len(combined_credit_df)}")
    
    # Display preview of combined credit file
    st.subheader("Combined Credit Card Data Preview")
    st.dataframe(combined_credit_df.head(10))
    
    # Download button for combined credit file
    csv_buffer = StringIO()
    combined_credit_df.to_csv(csv_buffer, index=False)
    csv_string = csv_buffer.getvalue()
    
    st.download_button(
        label="Download Combined Credit Card CSV",
        data=csv_string,
        file_name="combined_credit_cards.csv",
        mime="text/csv"
    )

# Display Debit Card Files
if debit_files:
    st.subheader("Debit Card Files Uploaded")
    for i, file in enumerate(debit_files):
        st.write(f"{i+1}. {file.name}")
        df = pd.read_csv(file)
        st.write(f"   - Rows: {len(df)}, Columns: {len(df.columns)}")
        st.dataframe(df.head(5))
