# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 120
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you finish entering stocks.\n")

# Step 1: Input from user
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("❗ Invalid stock symbol. Try again.")
        continue

    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("❗ Please enter a valid number.")

# Step 2: Calculate total investment
print("\n💼 Your Portfolio Summary:")
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        summary = f"{stock} - {qty} shares @ ${price} = ${value}"
        print(summary)
        file.write(summary + "\n")

    total_line = f"\nTotal Investment: ${total_investment}"
    print(total_line)
    file.write(total_line)

print("\n✅ Summary saved to 'portfolio_summary.txt'")
print("Thank you for using the Stock Portfolio Tracker! 📊")