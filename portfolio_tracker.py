# Smart Portfolio Tracker
# Adrian Pedersen

import yfinance as yf

print("\n=== Stock Portfolio Tracker ===")

ticker = input("Enter stock ticker: ").upper()
shares = float(input("Enter number of shares: "))
buy_price = float(input("Enter purchase price: "))

# Warning for 0 shares
if shares == 0:
    print("Warning: You entered 0 shares.")

# Get stock data
stock_data = yf.Ticker(ticker)
info = stock_data.info

current_price = info.get("currentPrice")

# Handle missing price
if current_price is None:
    print(f"Could not retrieve stock price for {ticker}")
else:
    # Calculations
    total_value = current_price * shares
    profit_loss = (current_price - buy_price) * shares
    percent_change = ((current_price - buy_price) / buy_price) * 100 if buy_price != 0 else 0

    # Round values
    current_price = round(current_price, 2)
    total_value = round(total_value, 2)
    profit_loss = round(profit_loss, 2)
    percent_change = round(percent_change, 2)

    # Output
    print("\n" + "-" * 30)
    print("--- Portfolio Summary ---")
    print(f"Ticker: {ticker}")
    print(f"Shares: {shares}")
    print(f"Buy Price: ${buy_price:.2f}")
    print(f"Current Price: ${current_price}")
    print(f"Total Value: ${total_value}")
    print(f"Profit/Loss: ${profit_loss}")
    print(f"Percent Change: {percent_change}%")
