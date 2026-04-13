import yfinance as yf

ticker = input("Enter stock ticker: ").upper()
shares = float(input("Enter number of shares: "))
buy_price = float(input("Enter purchase price: "))

stock = yf.Ticker(ticker)
info = stock.info

current_price = info.get("currentPrice")

if current_price is None:
    print(f"\nCould not find current price for ticker: {ticker}")
else:
    total_value = current_price * shares
    profit_loss = (current_price - buy_price) * shares

    print("\n--- Portfolio Summary ---")
    print(f"Ticker: {ticker}")
    print(f"Current Price: {current_price}")
    print(f"Total Value: {total_value}")
    print(f"Profit/Loss: {profit_loss}")
    