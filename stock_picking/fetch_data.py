import yfinance as yf
import numpy as np

def fetch_financial_data(ticker: str) -> dict:
    """
    Fetch financial data for a given ticker using yfinance.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple).

    Returns:
    dict: A dictionary containing the financial metrics required for Piotroski Score.
    """
    if not ticker:
        raise ValueError("Ticker symbol cannot be empty")

    # Fetch the company data
    stock = yf.Ticker(ticker)

    # info
    info = stock.info

    last_price = round(stock.history(period='1d')['Close'].iloc[0], 2)
    
    # Income statement
    income_stmt = stock.financials
    # print(income_stmt.T.columns)
    net_income = income_stmt.loc["Net Income"].iloc[0] if "Net Income" in income_stmt.index else 0
    net_income_prev = income_stmt.loc["Net Income"].iloc[1]  if "Net Income" in income_stmt.index else 0
    gross_profit = income_stmt.loc["Gross Profit"].iloc[0] if "Gross Profit" in income_stmt.index else 0
    gross_profit_prev = income_stmt.loc["Gross Profit"].iloc[1] if "Gross Profit" in income_stmt.index else 0
    total_revenue = income_stmt.loc["Total Revenue"].iloc[0] if "Total Revenue" in income_stmt.index else 0
    total_revenue_prev = income_stmt.loc["Total Revenue"].iloc[1] if "Total Revenue" in income_stmt.index else 0
    
    # Cash flow statement
    cashflow = stock.cashflow
    # print(cashflow.T.columns)
    operating_cash_flow = cashflow.loc["Cash Flow From Continuing Operating Activities"].iloc[0] if "Cash Flow From Continuing Operating Activities" in cashflow.index else 0
    operating_cash_flow_prev = cashflow.loc["Cash Flow From Continuing Operating Activities"].iloc[1] if "Cash Flow From Continuing Operating Activities" in cashflow.index else 0
    
    # Balance sheet
    balance_sheet = stock.balance_sheet
    # print(balance_sheet.T.columns)
    total_assets = balance_sheet.loc["Total Assets"].iloc[0] if "Total Assets" in balance_sheet.index else 0
    total_assets_prev = balance_sheet.loc["Total Assets"].iloc[1]  if "Total Assets" in balance_sheet.index else 0
    total_liabilities = balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]  if "Total Liabilities Net Minority Interest" in balance_sheet.index else 0
    total_liabilities_prev = balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[1]  if "Total Liabilities Net Minority Interest" in balance_sheet.index else 0
    current_assets = balance_sheet.loc["Current Assets"].iloc[0] if "Current Assets" in balance_sheet.index else 0
    current_liabilities = balance_sheet.loc["Current Liabilities"].iloc[0] if "Current Liabilities" in balance_sheet.index else 0
    current_assets_prev = balance_sheet.loc["Current Assets"].iloc[1] if "Current Assets" in balance_sheet.index else 0
    current_liabilities_prev = balance_sheet.loc["Current Liabilities"].iloc[1] if "Current Liabilities" in balance_sheet.index else 0
    shares_outstanding = stock.info['sharesOutstanding'] if 'sharesOutstanding' in stock.info.keys() else 0

    # Fetch Important ratios

    info = stock.info

    pb_ratio = info['priceToBook'] if 'priceToBook' in info.keys() else 0
    pe_ratio = info['trailingPE'] if 'trailingPE' in info.keys() else 0
    ps_ratio = info['priceToSalesTrailing12Months'] if 'priceToSalesTrailing12Months' in info.keys() else 0
    ev_to_ebitda = info['enterpriseToEbitda'] if 'enterpriseToEbitda' in info.keys() else 0
    ev_to_sales = info['enterpriseToRevenue'] if 'enterpriseToRevenue' in info.keys() else 0
    ev_to_ebit = info['enterpriseToEbitda'] if 'enterpriseToEbitda' in info.keys() else 0
    earnings_per_share = info['trailingEps'] if 'trailingEps' in info.keys() else 0
    dividend_yield = info['dividendYield'] if 'dividendYield' in info.keys() else 0
    quick_ratio = info['quickRatio'] if 'quickRatio' in info.keys() else 0
    current_ratio = info['currentRatio'] if 'currentRatio' in info.keys() else 0
    debt_to_equity = info['debtToEquity'] if 'debtToEquity' in info.keys() else 0

    
    # Calculations
    roa_current = net_income / total_assets  # Current ROA
    roa_previous = net_income_prev / total_assets_prev  # Previous ROA
    leverage_current = total_liabilities / total_assets  # Current leverage
    leverage_previous = total_liabilities_prev / total_assets_prev  # Previous leverage
    current_ratio_current = current_assets / current_liabilities if current_liabilities != 0 else 0
    current_ratio_previous = current_assets_prev / current_liabilities_prev if current_liabilities_prev != 0 else 0
    gross_margin_current = gross_profit / total_revenue if total_revenue != 0 else 0
    gross_margin_previous = gross_profit_prev / total_revenue_prev if total_revenue_prev != 0 else 0
    asset_turnover_current = total_revenue / total_assets if total_assets != 0 else 0
    asset_turnover_previous = total_revenue_prev / total_assets_prev if total_assets_prev != 0 else 0

    # Compile data into a dictionary
    financials = {
        "net_income": net_income,
        "operating_cash_flow": operating_cash_flow,
        "roa_current": roa_current,
        "roa_previous": roa_previous,
        "leverage_current": leverage_current,
        "leverage_previous": leverage_previous,
        "current_ratio_current": current_ratio_current,
        "current_ratio_previous": current_ratio_previous,
        "shares_outstanding_current": shares_outstanding,
        "shares_outstanding_previous": shares_outstanding,  # Assuming no dilution data from yfinance
        "gross_margin_current": gross_margin_current,
        "gross_margin_previous": gross_margin_previous,
        "asset_turnover_current": asset_turnover_current,
        "asset_turnover_previous": asset_turnover_previous,
        "PE Ratio": pe_ratio,
        "PB Ratio": pb_ratio,
        "PS Ratio": ps_ratio,
        "EV to EBITDA": ev_to_ebitda,
        "EV to Sales": ev_to_sales,
        "EV to EBIT": ev_to_ebit,
        "Earnings Per Share": earnings_per_share,
        "Dividend Yield": dividend_yield,
        "Quick Ratio": quick_ratio,
        "Current Ratio": current_ratio,
        "Debt to Equity": debt_to_equity,
        "Last Price": last_price,
        "Industry": info['industry'] if 'industry' in info.keys() else 'N/A',
        "Market Cap": info['marketCap'] if 'marketCap' in info.keys() else np.nan   
    }
    return financials
