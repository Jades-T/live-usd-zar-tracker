"""
Tests for the Data Extraction Module
These tests verify that the currency extraction functionality works correctly.
"""

import pytest
from data.extract_data import CurrencyExtractor

class TestCurrencyExtractor:
    """ Test class for CurrencyExtractor functionality."""

    def test_extraction_initialization(self):
        """ Test that checks if the extraction can be initialised."""
        extraction = CurrencyExtractor()
        assert extraction is not None
        assert extraction.base_url == "https://api.exchangerate-api.com/v4/latest/USD"

    def test_get_current_rate_structure(self):
        """ Test that checks if the current_rate turns the correct data structure."""
        extraction = CurrencyExtractor()
        result = extraction.get_current_rate()

        # The result should be None if the API fails, but if successul a dictionary.
        # Checks to see the structure of the currency data
        if result:
            assert isinstance(result, dict)
            assert 'rate' in result
            assert 'timestamp' in result
            assert 'base_currency' in result
            assert 'target_currency' in result
            assert result['base_currency'] == 'USD'
            assert result['target_currency'] == 'ZAR'
            assert isinstance(result['rate'], (int, float))
            assert result['rate'] > 0               # rate can never be -ve


    def test_get_current_rate_valid_values(self):
        """ Test that checks if the current_rate returns the valid values."""
        pass

    def test_get_historical_data_structure(self):
        """ Test that checks if the historical_datareturns the correct structure. """
        pass

    def test_get_historical_data_count(self):
        pass

    def test_get_historical_data_with_zero_days(self):
        pass


if __name__ == '__main__':
    pytest.main([__file__], "-v")