# SplitwiseBankApp

## File Combiner Tool

A Streamlit web application that allows users to upload multiple files and combine them into a single file. Perfect for merging CSV files, text files, or any text-based documents.

## Features

- **Multiple File Types**: Support for CSV files, text files, and any text-based files
- **CSV Combination Methods**:
  - **Concatenate**: Stack files vertically
  - **Concatenate with source**: Add source filename column to track data origin
  - **Merge**: Join files on common columns
- **Text File Combination**: Combine with custom separators between files
- **Download Options**: Download as CSV, Excel, or text files
- **File Preview**: See a preview of your combined data before downloading
- **User-friendly Interface**: Clean, modern Streamlit interface

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. **Select File Type**: Choose the type of files you want to combine from the sidebar
2. **Upload Files**: Use the file uploader to select multiple files
3. **Configure Options**: Set combination method and other options in the sidebar
4. **Combine Files**: Click the "Combine Files" button to process your files
5. **Download**: Download the combined result in your preferred format

## Supported File Types

- **CSV Files**: Spreadsheet data that can be concatenated, merged, or stacked
- **Text Files**: Plain text documents combined with custom separators
- **Any Text-based Files**: Any readable text files treated as plain text

## Examples

### CSV Files
- Combine monthly sales reports into a yearly report
- Merge customer data from different sources
- Stack transaction records with source tracking

### Text Files
- Combine multiple log files
- Merge documentation files
- Concatenate code snippets or notes

## Requirements

- Python 3.7+
- Streamlit 1.28.0+
- Pandas 2.0.0+
- openpyxl 3.0.10+ (for Excel export)
