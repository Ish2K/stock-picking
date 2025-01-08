def calculate_piotroski_score(financials):
    """
    Calculate the Piotroski Score based on a company's financial data.

    Parameters:
    financials (dict): Dictionary containing the following keys:
        - net_income (float): Net income of the company.
        - operating_cash_flow (float): Operating cash flow of the company.
        - roa_current (float): Return on assets (ROA) for the current year.
        - roa_previous (float): Return on assets (ROA) for the previous year.
        - leverage_current (float): Current year's leverage (debt-to-equity ratio).
        - leverage_previous (float): Previous year's leverage (debt-to-equity ratio).
        - current_ratio_current (float): Current ratio for the current year.
        - current_ratio_previous (float): Current ratio for the previous year.
        - shares_outstanding_current (float): Current year's number of shares outstanding.
        - shares_outstanding_previous (float): Previous year's number of shares outstanding.
        - gross_margin_current (float): Current year's gross margin.
        - gross_margin_previous (float): Previous year's gross margin.
        - asset_turnover_current (float): Current year's asset turnover ratio.
        - asset_turnover_previous (float): Previous year's asset turnover ratio.

    Returns:
    int: Piotroski Score (range: 0 to 9)
    """

    # check if all the required keys are present in the financials dictionary
    required_keys = ['net_income', 'operating_cash_flow', 'roa_current', 'roa_previous', 'leverage_current',
                     'leverage_previous', 'current_ratio_current', 'current_ratio_previous', 'shares_outstanding_current',
                     'shares_outstanding_previous', 'gross_margin_current', 'gross_margin_previous', 'asset_turnover_current',
                     'asset_turnover_previous', 'PE Ratio']
    for key in required_keys:
        if key not in financials:
            raise KeyError(f"Key '{key}' not found in financials dictionary")

    score = 0
    profitability_score = 0
    leverage_score = 0
    operating_efficiency_score = 0
    pe_ratio = 0

    # Profitability signals
    if financials['net_income'] > 0:
        profitability_score += 1  # Positive net income
    if financials['operating_cash_flow'] > 0:
        profitability_score += 1  # Positive operating cash flow
    if financials['operating_cash_flow'] > financials['net_income']:
        profitability_score += 1  # Operating cash flow > net income
    if financials['roa_current'] > financials['roa_previous']:
        profitability_score += 1  # ROA improvement

    # Leverage, Liquidity, and Source of Funds signals
    if financials['leverage_current'] < financials['leverage_previous']:
        leverage_score += 1  # Decreased leverage
    if financials['current_ratio_current'] > financials['current_ratio_previous']:
        leverage_score += 1  # Improved current ratio
    if financials['shares_outstanding_current'] <= financials['shares_outstanding_previous']:
        leverage_score += 1  # No dilution of shares

    # Operating Efficiency signals
    if financials['gross_margin_current'] > financials['gross_margin_previous']:
        operating_efficiency_score += 1  # Improved gross margin
    if financials['asset_turnover_current'] > financials['asset_turnover_previous']:
        operating_efficiency_score += 1  # Improved asset turnover ratio
    
    pe_ratio = financials['PE Ratio']

    return {
        "Profitablity": profitability_score,
        "Leverage": leverage_score,
        "Operating Efficiency": operating_efficiency_score,
        "Piotroski Score" : profitability_score + leverage_score + operating_efficiency_score
    }
