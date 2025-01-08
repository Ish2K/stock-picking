import pytest
from stock_picking.fetch_data import fetch_financial_data

def test_fetch_financial_data_valid_ticker():
    """
    Test fetching data for a valid stock ticker.
    """
    ticker = "AAPL"
    data = fetch_financial_data(ticker)
    
    # Ensure data is not None
    assert data is not None, f"Failed to fetch data for ticker {ticker}"

def test_fetch_financial_data_empty_ticker():
    """
    Test fetching data for an empty stock ticker.
    """
    ticker = ""
    with pytest.raises(ValueError, match="Ticker symbol cannot be empty"):
        fetch_financial_data(ticker)
