def stock_portfolio():
    stock_prices = {"AAPL": 180, "TSLA": 250, "MSFT": 300, "GOOG": 2800}
    portfolio = {}

    print("📈 Stock Portfolio Tracker")
    n = int(input("Enter number of stocks you own: "))

    for _ in range(n):
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        quantity = int(input("Enter quantity: "))

        if stock in stock_prices:
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        else:
            print("⚠️ Stock not found in price list!")

    total_value = sum(stock_prices[s] * q for s, q in portfolio.items())
    print("\nYour Portfolio:", portfolio)
    print("Total Investment Value: $", total_value)

    # Save results to file
    with open("portfolio.txt", "w") as f:
        f.write("Your Portfolio:\n")
        for s, q in portfolio.items():
            f.write(f"{s}: {q} shares\n")
        f.write(f"\nTotal Investment Value: ${total_value}\n")

    print("\n💾 Portfolio saved in 'portfolio.txt'")

if __name__ == "__main__":
    stock_portfolio()
