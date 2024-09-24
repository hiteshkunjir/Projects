create user STOCK_MARKET_ANALYSIS_SRC identified by Hitesh1999;

grant DBA to STOCK_MARKET_ANALYSIS_SRC;

grant all privileges to STOCK_MARKET_ANALYSIS_SRC;

CREATE TABLE stock_market_data (
    stock_symbol VARCHAR2(50),  -- Stock symbol, e.g., 'RELIANCE.BO'
    trade_date DATE,            -- Date of the stock data
    open_price NUMBER(10, 2),   -- Opening price of the stock
    high_price NUMBER(10, 2),   -- Highest price of the stock
    low_price NUMBER(10, 2),    -- Lowest price of the stock
    close_price NUMBER(10, 2),  -- Closing price of the stock
    volume NUMBER,              -- Volume of stock traded
    dividends NUMBER(10, 2),    -- Dividends for the stock
    stock_splits NUMBER(10, 2), -- Stock splits (if any)
    PRIMARY KEY (stock_symbol, trade_date)  -- Ensure no duplicate records for the same stock on the same date
);