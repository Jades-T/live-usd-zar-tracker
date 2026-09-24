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
        extraction = CurrencyExtractor()
        result = extraction.get_current_rate()

        if result:
            # Rate should be between 15-20 why?
            assert 15 < result['rate'] < 25

            # timestamp should be a string
            assert isinstance(result['timestamp'], str)

            # timestamp should have date information (date, time etc)
            assert len(result['rate']) > 0 

    def test_get_historical_data_structure(self):
        """ Test that checks if the historical_data returns the correct structure. """
        extraction = CurrencyExtractor()
        result = extraction.get_historical_data(days=5)

        assert isinstance(result, list)

        if result:
            # each data item should be a dict.
            for data in result:
                assert isinstance(data, dict)
                assert 'rate' in result
                assert 'timestamp' in result



    def test_get_historical_data_count(self):
        """ Test that checks for the return of the historical data, should be 5 days."""
        extraction = CurrencyExtractor()
        days = 5
        result = extraction.get_historical_data(days=days)

        if result:
            # SHoould return data for 5 days if working correctly.
            # if its less than 5, could be an API fail.
            assert len(result) <= days

    def test_get_historical_data_with_zero_days(self):
        """ Test that checks if historical data can be returned with zero day requests."""
        extraction = CurrencyExtractor()
        result = extraction.get_historical_data(days=0)

        # empty list should be returned.
        assert isinstance(result, list)


if __name__ == '__main__':
    pytest.main([__file__], "-v")