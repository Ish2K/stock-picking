import pytest
from stock_picking.piotroski_score import calculate_piotroski_score

def test_positive_piotroski_score():
    financials = {
        "net_income": 50000,
        "operating_cash_flow": 60000,
        "roa_current": 0.15,
        "roa_previous": 0.10,
        "leverage_current": 1.2,
        "leverage_previous": 1.5,
        "current_ratio_current": 1.8,
        "current_ratio_previous": 1.5,
        "shares_outstanding_current": 1000000,
        "shares_outstanding_previous": 1000000,
        "gross_margin_current": 0.45,
        "gross_margin_previous": 0.40,
        "asset_turnover_current": 1.2,
        "asset_turnover_previous": 1.0,
        "PE Ratio": 15
    }

    result = calculate_piotroski_score(financials)
    assert result["Profitablity"] == 4
    assert result["Leverage"] == 3
    assert result["Operating Efficiency"] == 2
    assert result["Piotroski Score"] == 9


def test_negative_piotroski_score():
    financials = {
        "net_income": -20000,
        "operating_cash_flow": -100000,
        "roa_current": 0.05,
        "roa_previous": 0.10,
        "leverage_current": 1.6,
        "leverage_previous": 1.2,
        "current_ratio_current": 1.2,
        "current_ratio_previous": 1.5,
        "shares_outstanding_current": 1100000,
        "shares_outstanding_previous": 1000000,
        "gross_margin_current": 0.30,
        "gross_margin_previous": 0.40,
        "asset_turnover_current": 0.9,
        "asset_turnover_previous": 1.0,
        "PE Ratio": 20
    }

    result = calculate_piotroski_score(financials)
    assert result["Profitablity"] == 0
    assert result["Leverage"] == 0
    assert result["Operating Efficiency"] == 0
    assert result["Piotroski Score"] == 0


def test_partial_piotroski_score():
    financials = {
        "net_income": 10000,
        "operating_cash_flow": 8000,
        "roa_current": 0.08,
        "roa_previous": 0.08,
        "leverage_current": 1.6,
        "leverage_previous": 1.5,
        "current_ratio_current": 1.4,
        "current_ratio_previous": 1.2,
        "shares_outstanding_current": 1050000,
        "shares_outstanding_previous": 1100000,
        "gross_margin_current": 0.35,
        "gross_margin_previous": 0.30,
        "asset_turnover_current": 1.0,
        "asset_turnover_previous": 1.1,
        "PE Ratio": 18
    }

    result = calculate_piotroski_score(financials)
    assert result["Profitablity"] == 2
    assert result["Leverage"] == 2
    assert result["Operating Efficiency"] == 1
    assert result["Piotroski Score"] == 5


def test_missing_fields():
    financials = {
        "net_income": 50000,
        "operating_cash_flow": 60000,
        # Missing 'roa_current' and 'roa_previous'
        "leverage_current": 1.2,
        "leverage_previous": 1.5,
        "current_ratio_current": 1.8,
        "current_ratio_previous": 1.5,
        "shares_outstanding_current": 1000000,
        "shares_outstanding_previous": 1000000,
        "gross_margin_current": 0.45,
        "gross_margin_previous": 0.40,
        "asset_turnover_current": 1.2,
        "asset_turnover_previous": 1.0,
        "PE Ratio": 15
    }

    with pytest.raises(KeyError):
        calculate_piotroski_score(financials)
