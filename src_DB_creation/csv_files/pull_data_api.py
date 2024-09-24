import yfinance as yf
import pandas as pd

# List of top 30 BSE companies' ticker symbols from Yahoo Finance (BSE)
top_30_bse_symbols = [
    'RELIANCE.BO', 'TCS.BO', 'HDFCBANK.BO', 'INFY.BO', 'ICICIBANK.BO',
    'HINDUNILVR.BO', 'KOTAKBANK.BO', 'SBIN.BO', 'BHARTIARTL.BO', 'HDFC.BO',
    'BAJFINANCE.BO', 'ITC.BO', 'LT.BO', 'AXISBANK.BO', 'ASIANPAINT.BO',
    'MARUTI.BO', 'ULTRACEMCO.BO', 'HCLTECH.BO', 'TECHM.BO', 'WIPRO.BO',
    'ONGC.BO', 'NTPC.BO', 'TITAN.BO', 'SUNPHARMA.BO', 'BAJAJFINSV.BO',
    'POWERGRID.BO', 'DRREDDY.BO', 'HEROMOTOCO.BO', 'COALINDIA.BO', 'TATASTEEL.BO'
]

def fetch_yfinance_data(symbols):
    for symbol in symbols:
        # Fetch data from Yahoo Finance
        stock = yf.Ticker(symbol)
        df = stock.history(period="max")
        
        # Check if data is available
        if df.empty:
            print(f"No data found for {symbol}")
            continue
        
        # Save the data to a CSV file
        output_file = f'{symbol}_market_data.csv'
        df.to_csv(output_file)
        print(f"Data for {symbol} saved to {output_file}")

if __name__ == "__main__":
    fetch_yfinance_data(top_30_bse_symbols)
