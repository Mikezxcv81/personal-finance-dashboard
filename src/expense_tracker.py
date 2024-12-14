import csv
import requests
from typing import List, Dict
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date: str, category: str, amount: float, description: str = ""):
        """Add a new transaction."""
        transaction = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        self.transactions.append(transaction)

    def load_transactions(self, file_path: str):
        """Load transactions from a CSV file."""
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            self.transactions.extend(reader)

    def save_transactions(self, file_path: str):
        """Save transactions to a CSV file."""
        with open(file_path, mode="w", newline="") as file:
            fieldnames = ["date", "category", "amount", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

    def get_summary(self) -> Dict[str, float]:
        """Summarize expenses by category."""
        summary = {}
        for transaction in self.transactions:
            category = transaction["category"]
            amount = float(transaction["amount"])
            summary[category] = summary.get(category, 0) + amount
        return summary

    def plot_expenses(self):
        """Visualize expenses using a bar chart."""
        summary = self.get_summary()

        categories = list(summary.keys())
        amounts = list(summary.values())

        # Create the bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(categories, amounts, color='skyblue')
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show the plot
        plt.show()

    def plot_expenses_pie(self):
        """Visualize expenses using a pie chart."""
        summary = self.get_summary()

        categories = list(summary.keys())
        amounts = list(summary.values())

        # Create the pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Expenses Distribution")
        plt.tight_layout()

        # Show the plot
        plt.show()

    def fetch_stock_price(self, symbol: str, api_key: str) -> float:
        """Fetch the latest stock price for a given symbol using Alpha Vantage API."""
        url = f"https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",
            "apikey": api_key
        }
        response = requests.get(url, params=params)
        data = response.json()

        try:
            latest_time = list(data["Time Series (1min)"].keys())[0]
            price = float(data["Time Series (1min)"][latest_time]["1. open"])
            return price
        except KeyError:
            raise ValueError(f"Error fetching stock price for {symbol}: {data.get('Note', 'Unknown error')}")

    def fetch_crypto_price(self, coin_id: str) -> float:
        """Fetch the current price of a cryptocurrency using CoinGecko API."""
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": coin_id,
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        data = response.json()

        try:
            price = data[coin_id]["usd"]
            return price
        except KeyError:
            raise ValueError(f"Error fetching cryptocurrency price for {coin_id}: {data}")
