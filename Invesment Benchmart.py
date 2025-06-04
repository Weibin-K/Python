import math
import matplotlib.pyplot as plt
import yfinance as yf

def get_rate_input(prompt):
    while True:
        rate_type = input(f"Is the {prompt} annual (A) or monthly (M)? ").strip().upper()
        if rate_type in ['A', 'M']:
            rate = float(input(f"Enter {prompt} rate (e.g., 0.06 for 6% annually or 0.005 for 0.5% monthly): "))
            if rate_type == 'A':
                rate /= 12
            return rate
        else:
            print("Please enter 'A' for annual or 'M' for monthly.")

def fetch_benchmark_returns(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="1y")  # 1 year daily data
    if hist.empty or len(hist) < 2:
        raise ValueError(f"Not enough data to compute returns for {ticker_symbol}")

    start_price = hist['Close'][0]
    end_price = hist['Close'][-1]
    annual_return = (end_price / start_price) - 1
    monthly_return = math.pow(1 + annual_return, 1/12) - 1

    return annual_return, monthly_return

def main():
    MAX_DECADES = 100
    
    initial_investment = float(input("Enter initial lump sum investment: "))
    monthly_contribution = float(input("Enter monthly contribution: "))
    
    dividend_rate = get_rate_input("dividend")
    growth_rate = get_rate_input("stock growth")
    
    total_months = int(input("Enter total number of months: "))
    reinvest_choice = input("Reinvest dividends? (Y/N): ").strip().upper()
    
    num_decades = (total_months + 119) // 120
    
    management_fees = []
    supp_charges = []
    for i in range(num_decades):
        mf = float(input(f"Enter monthly management fee rate (e.g., 0.000375 for 0.0375%) for years {i*10+1}-{(i+1)*10}: "))
        sc = float(input(f"Enter supplementary charge (as decimal, e.g., 0.05 for 5%) at end of year {(i+1)*10}: "))
        management_fees.append(mf)
        supp_charges.append(sc)
    
    print("\nFetching real-time benchmark data (this may take a moment)...")
    benchmarks = {
        "SPY": "SPY",
        "Gold ETF (GLD)": "GLD",
        "PIMCO Income Fund (PIMIX)": "PIMIX"
    }
    
    benchmark_returns = {}
    for name, ticker in benchmarks.items():
        try:
            ann_ret, mon_ret = fetch_benchmark_returns(ticker)
            benchmark_returns[name] = (ann_ret, mon_ret)
            print(f"{name}: Annual return ≈ {ann_ret*100:.2f}%, Monthly return ≈ {mon_ret*100:.3f}%")
        except Exception as e:
            print(f"Could not fetch data for {name} ({ticker}): {e}")
            # Fall back to zero returns if failure
            benchmark_returns[name] = (0.0, 0.0)
    
    balance = initial_investment
    total_invested = initial_investment
    total_dividends = 0.0
    total_fees = 0.0
    
    # Initialize benchmark balances
    spy_balance = initial_investment
    gold_balance = initial_investment
    pimco_balance = initial_investment
    
    months = []
    balances = []
    dividends_list = []
    growths_list = []
    fees_list = []
    total_invested_list = []
    
    for month in range(1, total_months + 1):
        current_decade = (month - 1) // 120
        
        balance += monthly_contribution
        total_invested += monthly_contribution
        
        dividend_earned = balance * dividend_rate
        growth_earned = balance * growth_rate
        fee_charged = balance * management_fees[current_decade]
        
        if reinvest_choice == 'Y':
            balance = balance + dividend_earned + growth_earned - fee_charged
        else:
            total_dividends += dividend_earned
            balance = balance + growth_earned - fee_charged
        
        total_fees += fee_charged
        
        if month % 120 == 0:
            decade_index = (month // 120) - 1
            charge = balance * supp_charges[decade_index]
            balance -= charge
            total_fees += charge
        
        # Update benchmark balances with monthly contribution and returns
        spy_balance = (spy_balance + monthly_contribution) * (1 + benchmark_returns["SPY"][1])
        gold_balance = (gold_balance + monthly_contribution) * (1 + benchmark_returns["Gold ETF (GLD)"][1])
        pimco_balance = (pimco_balance + monthly_contribution) * (1 + benchmark_returns["PIMCO Income Fund (PIMIX)"][1])
        
        months.append(month)
        balances.append(balance)
        dividends_list.append(dividend_earned)
        growths_list.append(growth_earned)
        fees_list.append(fee_charged)
        total_invested_list.append(total_invested)
    
    print("\n=== Investment Summary ===")
    print(f"Total invested: {total_invested:.2f}")
    print(f"Final portfolio value: {balance:.2f}")
    print(f"Total dividends earned: {total_dividends:.2f}")
    print(f"Total fees paid: {total_fees:.2f}")
    
    print("\n=== Benchmark Comparisons ===")
    print(f"SPY index final value: {spy_balance:.2f}")
    print(f"Gold ETF final value: {gold_balance:.2f}")
    print(f"PIMCO Income Fund final value: {pimco_balance:.2f}")
    
    plt.figure(figsize=(12, 6))
    plt.plot(months, balances, label='Portfolio Balance')
    plt.plot(months, [spy_balance]*len(months), '--', label='SPY Final Value')
    plt.plot(months, [gold_balance]*len(months), '--', label='Gold ETF Final Value')
    plt.plot(months, [pimco_balance]*len(months), '--', label='PIMCO Final Value')
    plt.xlabel("Month")
    plt.ylabel("Value")
    plt.title("Investment Portfolio vs Benchmarks Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.figure(figsize=(12, 6))
    plt.plot(months, dividends_list, label='Monthly Dividends')
    plt.plot(months, growths_list, label='Monthly Growth')
    plt.plot(months, fees_list, label='Monthly Fees')
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Monthly Earnings and Fees")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
