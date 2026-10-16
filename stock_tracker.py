
portfolio = []

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ")

    if stock_name.lower() == "done":
        break

    try:
        quantity = int(input("Enter quantity of shares: "))
        price = float(input("Enter price per share: "))

        if quantity <= 0 or price <= 0:
            print("Quantity and price must be positive!")
            continue

        investment = quantity * price

        stock = {
            "name": stock_name,
            "quantity": quantity,
            "price": price,
            "investment": investment
        }

        portfolio.append(stock)
        print("Stock added successfully!")

    except ValueError:
        print("Please enter a valid number.")

print("\n===== YOUR STOCK PORTFOLIO =====")

total_investment = 0

for stock in portfolio:
    print(
        stock["name"],
        "| Quantity:", stock["quantity"],
        "| Price:", stock["price"],
        "| Investment:", round(stock["investment"], 2)
    )
    total_investment += stock["investment"]

print("\nTotal Investment: ₹", round(total_investment, 2))
print("Thank you for using Stock Portfolio Tracker!")
