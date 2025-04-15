# Importing necessary libraries
import yfinance as yf  # This library allows us to fetch stock data from Yahoo Finance
import pandas as pd    # We'll use pandas for data handling (not strictly needed here but useful)

# Class that will handle our stock portfolio
class StockPortfolio:
    def __init__(self):
        # Initialize an empty portfolio (it's a dictionary)
        # The portfolio will store stock tickers as keys and their quantities as values.
        self.portfolio = {}
    
    def add_stock(self, ticker, quantity):
        """This method adds stocks to the portfolio."""
        # Check if the stock already exists in the portfolio
        if ticker in self.portfolio:
            # If the stock exists, increase the quantity by the specified amount
            self.portfolio[ticker]['quantity'] += quantity
        else:
            # If the stock doesn't exist, add it with the specified quantity
            self.portfolio[ticker] = {'quantity': quantity}
        print(f"Added {quantity} shares of {ticker} to your portfolio.")
    
    def remove_stock(self, ticker, quantity):
        """This method removes stocks from the portfolio."""
        if ticker in self.portfolio:
            # Check if there are enough shares to remove
            if self.portfolio[ticker]['quantity'] >= quantity:
                self.portfolio[ticker]['quantity'] -= quantity
                print(f"Removed {quantity} shares of {ticker} from your portfolio.")
            else:
                print(f"Not enough shares of {ticker} to remove {quantity} shares.")
        else:
            print(f"{ticker} is not in your portfolio.")
    
    def get_current_stock_price(self, ticker):
        """This method fetches the real-time stock price for a given ticker."""
        try:
            # Fetch stock data from Yahoo Finance using the 'yfinance' library
            stock = yf.Ticker(ticker)
            # Get the historical stock data for the last day and retrieve the closing price
            data = stock.history(period="1d")
            return data['Close'][0]  # We just need the closing price of the last trading day
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None
    
    def track_portfolio_value(self):
        """This method tracks and calculates the total value of the portfolio."""
        total_value = 0  # This will store the total value of the portfolio
        # Loop through each stock in the portfolio
        for ticker, stock_info in self.portfolio.items():
            # Get the current price of the stock
            current_price = self.get_current_stock_price(ticker)
            if current_price:
                # Calculate the total value of that stock in the portfolio (Price * Quantity)
                stock_value = current_price * stock_info['quantity']
                total_value += stock_value
                print(f"{ticker}: {stock_info['quantity']} shares, Current Price: ${current_price:.2f}, Value: ${stock_value:.2f}")
        
        # Print the total value of all stocks in the portfolio
        print(f"Total Portfolio Value: ${total_value:.2f}")
    
    def display_portfolio(self):
        """This method displays the stocks and their quantities in the portfolio."""
        if not self.portfolio:
            print("Your portfolio is empty.")
        else:
            for ticker, stock_info in self.portfolio.items():
                print(f"{ticker}: {stock_info['quantity']} shares")

# Main function to run the portfolio tracker
def main():
    # Create an instance of the StockPortfolio class
    portfolio = StockPortfolio()
    
    while True:
        # Print the options menu
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock to Portfolio")
        print("2. Remove Stock from Portfolio")
        print("3. View Portfolio")
        print("4. Track Portfolio Value")
        print("5. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # If the user wants to add stock
            ticker = input("Enter the stock ticker (e.g., AAPL for Apple): ").upper()
            quantity = int(input(f"Enter the number of shares of {ticker}: "))
            portfolio.add_stock(ticker, quantity)
        
        elif choice == '2':
            # If the user wants to remove stock
            ticker = input("Enter the stock ticker (e.g., AAPL for Apple): ").upper()
            quantity = int(input(f"Enter the number of shares of {ticker} to remove: "))
            portfolio.remove_stock(ticker, quantity)
        
        elif choice == '3':
            # If the user wants to view the current portfolio
            portfolio.display_portfolio()
        
        elif choice == '4':
            # If the user wants to track the portfolio's value
            portfolio.track_portfolio_value()
        
        elif choice == '5':
            # If the user wants to exit the program
            print("Exiting the Stock Portfolio Tracker. Goodbye!")
            break
        
        else:
            # If the user entered an invalid option
            print("Invalid choice. Please try again.")

# Run the main function to start the portfolio tracker
if __name__ == "__main__":
    main()
