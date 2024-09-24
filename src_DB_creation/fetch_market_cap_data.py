import pandas as pd
import requests
import cx_Oracle

# Function to fetch market cap data for top 30 BSE companies
def fetch_market_cap_data():
    symbols = ["RELIANCE", "TCS", "HDFC", "INFY", "HINDUNILVR", "ICICIBANK", "KOTAKBANK",
               "LT", "SBIN", "BAJFINANCE", "ITC", "AXISBANK", "TITAN", "MARUTI", 
               "M&M", "ONGC", "ASIANPAINT", "NTPC", "POWERGRID", "BAJAJ-AUTO", 
               "SUNPHARMA", "ULTRACEMCO", "CIPLA", "HCLTECH", "JSWSTEEL", "GRASIM", 
               "ADANIGREEN", "DRREDDY", "WIPRO", "TATASTEEL"]

    data = []

    for symbol in symbols:
        url = f"https://finance.yahoo.com/quote/{symbol}.BO"
        response = requests.get(url)

        # Extract company name, sector, and market cap from the response (example extraction)
        # This should be adjusted based on the actual structure of the Yahoo Finance response
        # For demonstration purposes, using placeholder values
        company_name = f"{symbol} Limited"  # Placeholder
        sector = "Financial Services"  # Placeholder
        market_cap = 0  # Placeholder

        # Insert your logic to fetch the actual market cap from the response

        # Append the data with symbol in uppercase
        data.append({
            "stock_id": f"S{str(len(data) + 1).zfill(3)}",
            "symbol": symbol.upper(),
            "company_name": company_name,
            "sector": sector,
            "market_cap": market_cap
        })

    return pd.DataFrame(data)

# Main execution
if __name__ == "__main__":
    df = fetch_market_cap_data()

    # Save to CSV
    csv_file_name = 'stocks_dim.csv'
    df.to_csv(csv_file_name, index=False)

    print(f"CSV file '{csv_file_name}' created stocks_dim.csv file successfully!")
