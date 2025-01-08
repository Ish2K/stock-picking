import pandas as pd
from stock_picking.piotroski_score import calculate_piotroski_score
from stock_picking.fetch_data import fetch_financial_data

def get_top_stocks(
        tickers: str | list[str],
        exchange: str = 'NYSE', 
        stock_return_threshold : float = 0.045,
        piotroski_score_threshold : int = 7,
        market_cap_threshold : float = 1e9,
        sort_by : str|list[str] = ['Industry','Stock Return %'],
        sort_precedence : bool|list[bool] = [True, False],
        generate_csv : bool = True,
        file_path : str = 'top_stocks.csv'
    ) -> pd.DataFrame:
    """
    Fetch the top stocks based on the Piotroski Score and EPS / Last Price.

    Parameters:
    tickers (str or list): If a string, it should be a path to csv file containing "Symbol" column.
        If a list, it should contain stock ticker symbols.
    exchange (str): The stock exchange to fetch the data from - It can either be NSE or NYSE.
    stock_return_threshold (float): The threshold for the EPS / Last Price ratio (risk free return).
    piotroski_score_threshold (int): The minimum Piotroski Score required for a stock to be considered.
    market_cap_threshold (float): The minimum market capitalization required for a stock to be considered.
    sort_by (str or list): The column(s) to sort the top stocks by.
    sort_precedence (bool or list): The sort order for the columns specified in sort_by.
    generate_csv (bool): If True, a CSV file containing the top stocks will be generated. 
    file_path (str): The path to the CSV file where the top stocks will be saved.  

    Returns:
    str or list: If a string is provided as input, the function returns the stock ticker symbol of the top stock.
        If a list is provided, the function returns a list of stock ticker symbols of the top stocks.
    """
    
    if isinstance(tickers, str):
        tickers = pd.read_csv(tickers)
        tickers = tickers['Symbol'].tolist()

    tickers = list(set(tickers))

    if(exchange == 'NSE'):
        tickers = [ticker + '.NS' for ticker in tickers]

    ticker_financials = dict()

    for ticker in tickers:
        try:
            financials = fetch_financial_data(ticker)
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            continue
        piotroski_score = calculate_piotroski_score(financials)
        industry = financials['Industry']
        marketCap = financials['Market Cap']
        eps = financials['Earnings Per Share']
        last_price = financials['Last Price']
        eps_last_price_ratio = eps / last_price

        if ((eps_last_price_ratio >= stock_return_threshold) and (piotroski_score["Piotroski Score"] >= piotroski_score_threshold) and (marketCap >= market_cap_threshold)):
            ticker_financials[ticker] = {
                "Ticker": ticker,
                "Industry": industry,
                "Market Cap": marketCap,
                "Stock Return %": eps_last_price_ratio * 100,
                "Profitablity": piotroski_score['Profitablity'],
                "Leverage": piotroski_score['Leverage'],
                "Operating Efficiency": piotroski_score['Operating Efficiency'],
                "Piotroski Score": piotroski_score["Piotroski Score"],
            }
    
    df = pd.DataFrame(ticker_financials).T
    df = df.sort_values(by = sort_by, ascending = sort_precedence)

    if generate_csv:
        assert file_path.endswith('.csv'), "File path should end with .csv"
        df.to_csv(file_path, index = False)
    
    return df
