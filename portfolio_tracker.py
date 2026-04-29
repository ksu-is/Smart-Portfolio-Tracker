import yfinance as yf

portfolio = []

print("=== Stock Portfolio Tracker ===")

while True:
    ticker = input("\nEnter stock ticker or type DONE to finish: ").upper()

    if ticker == "DONE":
        break

    shares = float(input("Enter number of shares: "))
    buy_price = float(input("Enter purchase price: "))

    stock = yf.Ticker(ticker)
    info = stock.info
    current_price = info.get("currentPrice")

    if current_price is None:
        print(f"Could not find current price for {ticker}. Try another ticker.")
        continue

    total_cost = shares * buy_price
    current_value = shares * current_price
    profit_loss = current_value - total_cost
    percent_change = (profit_loss / total_cost) * 100 if total_cost != 0 else 0

    portfolio.append({
        "ticker": ticker,
        "shares": shares,
        "buy_price": buy_price,
        "current_price": current_price,
        "total_cost": total_cost,
        "current_value": current_value,
        "profit_loss": profit_loss,
        "percent_change": percent_change
    })

print("\n=== Portfolio Summary ===")

portfolio_total_cost = 0
portfolio_current_value = 0
portfolio_profit_loss = 0

for stock in portfolio:
    print("\n------------------------")
    print(f"Ticker: {stock['ticker']}")
    print(f"Shares: {stock['shares']}")
    print(f"Buy Price: ${stock['buy_price']:.2f}")
    print(f"Current Price: ${stock['current_price']:.2f}")
    print(f"Total Cost: ${stock['total_cost']:.2f}")
    print(f"Current Value: ${stock['current_value']:.2f}")
    print(f"Profit/Loss: ${stock['profit_loss']:.2f}")
    print(f"Percent Change: {stock['percent_change']:.2f}%")

    portfolio_total_cost += stock["total_cost"]
    portfolio_current_value += stock["current_value"]
    portfolio_profit_loss += stock["profit_loss"]

print("\n=== Total Portfolio Results ===")
print(f"Total Cost: ${portfolio_total_cost:.2f}")
print(f"Total Current Value: ${portfolio_current_value:.2f}")
print(f"Total Profit/Loss: ${portfolio_profit_loss:.2f}")

import json

with open("portfolio.json", "w") as f:
    json.dump(portfolio, f, indent=4)

print("\nPortfolio saved to portfolio.json")

