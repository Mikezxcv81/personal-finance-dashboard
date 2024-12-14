from src.expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    # Load sample data
    tracker.load_transactions("data/sample_transactions.csv")
    print("Transactions loaded.")

    # Add a new transaction
    tracker.add_transaction("2024-01-15", "Groceries", 75.0, "Additional shopping")
    print("New transaction added.")

    # Save to a new file
    tracker.save_transactions("data/updated_transactions.csv")
    print("Transactions saved to 'data/updated_transactions.csv'.")

    # Display summary
    summary = tracker.get_summary()
    print("\nExpense Summary:")
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")

    # Fetch real-time stock price
    alpha_vantage_api_key = "<7GI70WCI86VQBK6J>"
    try:
        stock_price = tracker.fetch_stock_price("AAPL", alpha_vantage_api_key)
        print(f"\nReal-time Stock Price for AAPL: ${stock_price:.2f}")
    except ValueError as e:
        print(e)

    # Fetch real-time cryptocurrency price
    try:
        crypto_price = tracker.fetch_crypto_price("bitcoin")
        print(f"\nReal-time Cryptocurrency Price for Bitcoin: ${crypto_price:.2f}")
    except ValueError as e:
        print(e)

    # Plot expenses
    print("\nDisplaying bar chart for expenses...")
    tracker.plot_expenses()

    # Plot pie chart
    print("\nDisplaying pie chart for expenses...")
    tracker.plot_expenses_pie()

if __name__ == "__main__":
    main()
