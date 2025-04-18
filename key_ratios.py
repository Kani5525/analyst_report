# %%
import yfinance as yf

# Prompt user for ticker symbol
TICKER = input("Enter stock ticker (e.g., PPT.AX): ").upper()

try:
    # Ensure TICKER is not empty
    if not TICKER:
        raise ValueError("Ticker symbol cannot be empty.")

    # Get stock data
    stock = yf.Ticker(TICKER)
    stock_prices = stock.history(period="5y")
    stock_info = stock.info
    stock_financials = stock.financials
    stock_balance_sheet = stock.balance_sheet

    # Extract data
    last_price = stock_prices['Close'].iloc[-1]
    earnings = stock_financials.loc["Net Income"].iloc[0]
    dividend = stock_info.get('lastDividendValue', 0)
    shares_outstanding = stock_info['sharesOutstanding']
    total_assets = (
        stock_balance_sheet.loc["Total Assets"].iloc[0] +
        stock_balance_sheet.loc["Total Assets"].iloc[1]
    ) / 2

    # Calculate ratios
    # Define the calculate_dividend_yield function
    def calculate_dividend_yield(dividend, price):
        if price == 0:
            return 0
        return dividend / price

    dividend_yield = calculate_dividend_yield(dividend, last_price) * 100
    # Define the calculate_eps function
    def calculate_eps(earnings, shares_outstanding):
        if shares_outstanding == 0:
            return 0
        return earnings / shares_outstanding

    eps = calculate_eps(earnings, shares_outstanding)
    # Define the calculate_pe_ratio function
    def calculate_pe_ratio(price, eps):
        if eps == 0:
            return float('inf')  # Return infinity if EPS is zero to avoid division by zero
        return price / eps

    pe_ratio = calculate_pe_ratio(last_price, eps)
    # Define the calculate_roa function
    def calculate_roa(earnings, total_assets):
        if total_assets == 0:
            return 0
        return earnings / total_assets

    roa = calculate_roa(earnings, total_assets) * 100

    # Print summary
    print(f"\nChosen Stock: {TICKER}")
    print(f"Last Share Price: ${last_price:.2f}")
    print(f"PE Ratio: {pe_ratio:.4f}")  # More precision to avoid -0.00 confusion
    print(f"Dividend Yield: {dividend_yield:.2f}%")
    print(f"EPS: {eps:.2f}")
    print(f"ROA: {roa:.2f}%")

except Exception as e:
    print(f"Error: {e}")

def get_financial_summary(ticker, last_price, pe_ratio, dividend_yield, eps, roa):
    summary = {
        "Chosen Stock": ticker,
        "Last Share Price": f"${last_price:.2f}",
        "PE Ratio": f"{pe_ratio:.4f}",
        "Dividend Yield": f"{dividend_yield:.2f}%",
        "EPS": f"{eps:.2f}",
        "ROA": f"{roa:.2f}%"
    }
    return summary
print(get_financial_summary(TICKER, last_price, pe_ratio, dividend_yield, eps, roa))

# %%
