import pytest
import pandas as pd

from backend import get_available_countries, get_country_data, format_number

def test_get_available_countries():
    countries = get_available_countries()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert "US" in countries
    assert "Europe" in countries
    assert "China" in countries
    
def test_get_country_data():
    data = get_country_data()
    assert data.size > 0
    assert isinstance(data, pd.DataFrame)
    
    data = get_country_data(["US"])
    assert data.size > 0
    assert isinstance(data, pd.DataFrame)
    
def test_get_country_data_bad_country():
    with pytest.raises(ValueError):
        get_country_data(["NonExistentCountry"])

def test_format_number():
    assert format_number(1000) == "1,000"
    assert format_number(1234567.89) == "1,234,567.89"

def test_format_number_invalid_type():
    with pytest.raises(ValueError):
        format_number("string")