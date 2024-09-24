import pandas as pd
import os
import cx_Oracle

csv_directory = r"C:\Users\Hitesh\Desktop\Projects\Stock_market_analysis\src_DB_creation\csv_files"

# Create a database connection
connection = cx_Oracle.connect('STOCK_MARKET_ANALYSIS_SRC', 'Hitesh1999', 'localhost:1521/XE')
cursor = connection.cursor()

# Load CSV files
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(file_path)

        # Print columns to check available data
        print(f"Loaded data from {file_path}")
        print(df.columns)  # Check what columns are present

        # Extract stock symbol from the filename
        stock_symbol = filename.split('.')[0]  # Assuming the format is 'SYMBOL.BO_market_data.csv'

        # Insert data into the database
        for index, row in df.iterrows():
            # Convert Date to the correct format
            trade_date = pd.to_datetime(row['Date']).date()  # Use .date() to get only the date part

            # Ensure numerical values are in the correct format
            open_price = float(row['Open'])
            high_price = float(row['High'])
            low_price = float(row['Low'])
            close_price = float(row['Close'])
            volume = int(row['Volume']) if pd.notnull(row['Volume']) else 0  # Handle NaN values
            dividends = float(row['Dividends']) if pd.notnull(row['Dividends']) else 0.0
            stock_splits = float(row['Stock Splits']) if pd.notnull(row['Stock Splits']) else 0.0
            
            # Debugging output
            print(f"Trade Date: {trade_date}, Open Price: {open_price}, High Price: {high_price}, Low Price: {low_price}, Close Price: {close_price}, Volume: {volume}, Dividends: {dividends}, Stock Symbol: {stock_symbol}, Stock Splits: {stock_splits}")
            
            # Insert into database
            try:
                cursor.execute(
                    "INSERT INTO stock_market_data (TRADE_DATE, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, VOLUME, DIVIDENDS, STOCK_SYMBOL, STOCK_SPLITS) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)",
                    (trade_date, open_price, high_price, low_price, close_price, volume, dividends, stock_symbol, stock_splits)
                )
            except cx_Oracle.DatabaseError as e:
                error, = e.args
                print(f"Error Code: {error.code}, Error Message: {error.message}")

# Commit and close connection
connection.commit()
cursor.close()
connection.close()
