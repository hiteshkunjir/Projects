


INSERT INTO Date_Dim (date_id, date_value, year, month, day_of_month, day_of_week, quarter)
SELECT DISTINCT TO_CHAR(trade_date, 'DDMMYYYY') AS date_id,  -- Generate date_id in DDMMYYYY format
       trade_date AS date_value,
       TO_CHAR(trade_date, 'YYYY') AS year,         -- Extract year
       TO_CHAR(trade_date, 'MM') AS month,          -- Extract month
       TO_CHAR(trade_date, 'DD') AS day_of_month,   -- Extract day of the month
       TO_CHAR(trade_date, 'DAY') AS day_of_week,   -- Extract day of the week
       CASE                                         -- Calculate quarter based on month
           WHEN TO_CHAR(trade_date, 'MM') IN ('01', '02', '03') THEN '1'
           WHEN TO_CHAR(trade_date, 'MM') IN ('04', '05', '06') THEN '2'
           WHEN TO_CHAR(trade_date, 'MM') IN ('07', '08', '09') THEN '3'
           WHEN TO_CHAR(trade_date, 'MM') IN ('10', '11', '12') THEN '4'
           ELSE NULL
       END AS quarter
FROM STOCK_MARKET_ANALYSIS_SRC.stock_market_data
WHERE trade_date IS NOT NULL
  AND TO_CHAR(trade_date, 'DDMMYYYY') NOT IN (SELECT date_id FROM Date_Dim) order by date_value;
  
INSERT INTO Stock_Prices_Fact (stock_id, date_id, open_price, close_price, high_price, low_price, volume)
SELECT 
    sd.stock_id, 
    dd.date_id, 
    sm.open_price, 
    sm.close_price, 
    sm.high_price, 
    sm.low_price, 
    sm.volume
FROM 
    Stocks_Dim sd
JOIN 
    STOCK_MARKET_ANALYSIS_SRC.stock_market_data sm ON sm.stock_symbol = sd.symbol
JOIN 
    Date_Dim dd ON sm.trade_date = dd.date_value;

