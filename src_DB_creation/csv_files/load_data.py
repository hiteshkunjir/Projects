import os
import cx_Oracle
import pandas as pd

# Database connection
connection = cx_Oracle.connect("username/password@database")
cursor = connection.cursor()

# Directory containing CSV files
csv_directory = "/path/to/csv/files"

# Loop through CSV files
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        stock_symbol = filename.split('_')[0]  # Extract stock symbol from the filename

        # Load CSV data into a pandas DataFrame
        df = pd.read_csv(os.path.join(csv_directory, filename))
        
        # Insert data row by row into the Oracle table
        for index, row in df.iterrows():
            cursor.execute("""
                INSERT INTO stock_market_data (trade_date, open_price, high_price, low_price, close_price, volume, dividends, stock_symbol, stock_splits)
                VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4, :5, :6, :7, :8, :9)""",
                (row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Dividends'], stock_symbol, row['Splits'])
            )

# Commit and close the connection
connection.commit()
cursor.close()
connection.close()
