import os
import streamlit as st
import pandas as pd
import io
from typing import List, Dict, Any
from datetime import date, timedelta


# Create sidebar that allows users to upload credit card transactions as csv files
st.sidebar.header("Upload Credit Card Transactions")
credit_files = st.sidebar.file_uploader("Choose credit CSV files", accept_multiple_files=True, type=["csv"])

st.sidebar.header("Upload Debit Card Transactions")
debit_files = st.sidebar.file_uploader("Choose debit xlsx files", accept_multiple_files=True, type=["xlsx"])

st.sidebar.header("Select Dates")
today = date.today()
thirty_days_ago = today - timedelta(days=30)
date_range = st.sidebar.date_input("Select date range", [thirty_days_ago, today])


# Create a function to read and combine credit card transaction files
def load_credit_transaction_data(files: List[io.BytesIO]) -> pd.DataFrame:
    dataframes = []
    for file in files:
        df = pd.read_csv(file)
        
        # Drop Memo column, and filter by Type == Sale
        df = df.drop(columns=["Memo"], errors="ignore")
        df = df[df["Type"] == "Sale"]
        
        # Add a shared column and default everything to yes
        df["Shared"] = "Yes"
        df["cardType"] = "Credit"
        
        # Multiply Amount by -1 to make amount positive
        df["Amount"] = df["Amount"] * -1
        
        # Make Transaction Date and Post Date datetime
        df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
        df["Post Date"] = pd.to_datetime(df["Post Date"])   

       # Only Keep Transaction Date, Post Date ,Description, Category ,Amount, and Shared
        df = df[["Transaction Date", "Post Date", "Description", "Category", "Amount", "Shared"]]

        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

# Create function to load debit card transactions
def load_debit_transaction_data(files: List[io.BytesIO]) -> pd.DataFrame:
    dataframes = []
    for file in files:
        df = pd.read_excel(file)
  
# Add a shared column and default everything to No
        df["Shared"] = "No"
        df["cardType"] = "Debit"

        # Multiply Amount by -1 to make amount positive
        df["Amount"] = df["Amount"] * -1
        
        # Make Posting Date a datetime
        df["Posting Date"] = pd.to_datetime(df["Posting Date"])

        # Only keep Posting Date, Description, Amount, and Shared
        df = df[["Posting Date", "Description", "Amount", "Shared"]]

        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

# Cache data loading
cc_files = load_credit_transaction_data(credit_files) if credit_files else pd.DataFrame()
dc_files = load_debit_transaction_data(debit_files) if debit_files else pd.DataFrame()




st.header("Credit Card Transactions")

# Show credit card filtered data in a data editor, in the filtered date range if specified
start_date, end_date = date_range

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)


# Display info only if data is uploaded
if date_range and cc_files is not None and dc_files is not None and not cc_files.empty and not dc_files.empty:

    # Filtered cc files
    filtered_cc_files = cc_files[(cc_files["Transaction Date"] >= start_date) & (cc_files["Transaction Date"] <= end_date)]
    filtered_edited_cc = st.data_editor(filtered_cc_files, key="credit_card_transactions", height=300, use_container_width=True)
    
    st.header("Debit Card Transactions")
    filtered_dc_files = dc_files[(dc_files["Posting Date"] >= start_date) & (dc_files["Posting Date"] <= end_date)]
    filtered_edited_dc = st.data_editor(filtered_dc_files, key="debit_card_transactions", height=300, use_container_width=True)

    # Show metrics for filtered data
    st.header("Spending Breakdown")

    col1, col2 = st.columns(2)

    # Get total shared spending between credit and debit cards based on filtered date range using a metric
    with col1:
        total_shared = filtered_edited_cc[filtered_edited_cc["Shared"] == "Yes"]["Amount"].sum() + \
            filtered_edited_dc[filtered_edited_dc["Shared"] == "Yes"]["Amount"].sum()
        st.metric("Total Shared Spending", f"${total_shared:,.2f}")

    # Get total non-shared spending between credit and debit cards based on filtered date range using a metric
    with col2:
        total_non_shared = filtered_edited_cc[filtered_edited_cc["Shared"] == "No"]["Amount"].sum() + \
            filtered_edited_dc[filtered_edited_dc["Shared"] == "No"]["Amount"].sum()
        st.metric("Total Non-Shared Spending", f"${total_non_shared:,.2f}")
        
else:
    st.info("Please upload credit and debit card transaction files to see the data and spending breakdown.")
        

