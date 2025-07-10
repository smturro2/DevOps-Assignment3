import pandas as pd


full_table = pd.DataFrame(
    index=["US", "Europe", "China"],
    columns=["Population", "GDP", "Debt"],
    data=[
        [331002651, 21137518, 28141300000000],
        [747636026, 15546200000000, 13000000000000],
        [1439323776, 14342903, 9800000000000]
    ]
)

def get_country_data(countries=None):
    if countries is None:
        countries = get_available_countries()
        
    for c in countries:
        if c not in full_table.index:
            raise ValueError(f"Country {c} not found in data")
    
    return full_table.loc[countries].copy()


def get_available_countries():
    return ["US", "Europe", "China"]
    
def format_number(x):
    if isinstance(x, int):
        return f"{x:,}"
    elif isinstance(x, float):
        return f"{x:,.2f}"
    raise ValueError("Unsupported type for formatting")