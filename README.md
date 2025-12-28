# SplitwiseBankApp
This app takes debit and credit card transaction csvs and allows users to specify which transactions are shared and which allowing you to sum them up.

## Features
- Upload multiple credit card CSV files
- Upload multiple debit card CSV files
- Automatically combine all credit card files into one consolidated file
- Preview uploaded data
- Download the combined credit card CSV file

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown (typically `http://localhost:8501`)

3. Upload your CSV files:
   - Use the "Credit Card Files" section to upload one or more credit card CSV files
   - Use the "Debit Card Files" section to upload one or more debit card CSV files

4. The app will automatically:
   - Combine all credit card files into one
   - Display a preview of the combined data
   - Provide a download button for the combined credit card CSV

## CSV Format
Your CSV files should include transaction data with columns such as:
- Date
- Description
- Amount
- Category

The app will preserve all columns from your input files. 
