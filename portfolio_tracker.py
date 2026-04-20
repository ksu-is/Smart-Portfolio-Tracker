import yfinance as yf

portfolio = []

while True:
    ticker = input("Enter stock ticker (or type 'done' to finish): ").upper()
    
    if ticker == "DONE":
        break

    shares = float(input("Enter number of shares: "))
    buy_price = float(input("Enter purchase price: "))

    stock = yf.Ticker(ticker)
    info = stock.info
    current_price = info.get("currentPrice")

    if current_price is None:
        print(f"Could not find price for {ticker}\n")
        continue

    portfolio.append({
        "ticker": ticker,
        "shares": shares,
        "buy_price": buy_price,
        "current_price": current_price
    })

print("\n--- Portfolio Summary ---")

total_value = 0
total_profit = 0

for stock in portfolio:
    value = stock["shares"] * stock["current_price"]
    profit = (stock["current_price"] - stock["buy_price"]) * stock["shares"]

    total_value += value
    total_profit += profit

    print(f"\nTicker: {stock['ticker']}")
    print(f"Shares: {stock['shares']}")
    print(f"Current Price: {stock['current_price']:.2f}")
    print(f"Value: {value:.2f}")
    print(f"Profit/Loss: {profit:.2f}")

print("\n--- Total Portfolio ---")
print(f"Total Value: {total_value:.2f}")
print(f"Total Profit/Loss: {total_profit:.2f}")
    
