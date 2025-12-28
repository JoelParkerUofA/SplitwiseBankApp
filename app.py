import streamlit as st
import pandas as pd
import io
from typing import List, Dict, Any


# Create sidebar that allows users to upload credit card transactions as csv files
st.sidebar.header("Upload Credit Card Transactions")
credit_files = st.sidebar.file_uploader("Choose credit CSV files", accept_multiple_files=True, type=["csv"])

st.sidebar.header("Upload Debit Card Transactions")
debit_files = st.sidebar.file_uploader("Choose debit CSV files", accept_multiple_files=True, type=["csv"])


# Create a function to read and combine credit card transaction files
def load_credit_transaction_data(files: List[io.BytesIO]) -> pd.DataFrame:
    dataframes = []
    for file in files:
        df = pd.read_csv(file)
        dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)

cc_files = load_credit_transaction_data(credit_files) if credit_files else pd.DataFrame()

st.data_editor(cc_files, key="credit_card_transactions", height=300, use_container_width=True)