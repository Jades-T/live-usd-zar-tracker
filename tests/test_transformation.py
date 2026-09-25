"""
Tests for the Data Transformation Module
These tests verify that data cleaning and transformation work correctly.
"""
import pytest
import pandas as pd
from src.data.transform_data import DataTransformer

class TestDataTransformer:
    """ Test class for the transformation of data."""

    @pytest.fixture
    def transformer(self):
        """ This creates a DataTransformer instance for testing. """
        return DataTransformer()

    def test_transformer_initialization(self, transformer):
        """ Test that checks if transformer can be initialized."""
        assert transformer is not None
        assert 'USD' in transformer.valid_currencies
        assert 'ZAR' in transformer.valid_currencies


    def test_clean_rate_data_valid_rate(self, transformer):
        """ Test to check for cleaning valid rate data."""
        valid_data = {
            'rate': 18.5,
            'timestamp': '2026-09-21 10:00:00',
            'base_currency': 'USD',
            'target_currency': 'ZAR'
        }

        result = transformer.clean_rate_valid_data(valid_data)

        assert result is not None
        assert result['rate'] == 18.5
        assert result['base_currency'] == 'USD'
        assert result['target_currency'] == 'ZAR'

    def test_clean_rate_data_invalid_rate(self, transformer):
        """ Test cleaning data with invalid rate."""
        invalid_rate = {
            'rate': -5, # negative rate, seems odd right?
            'timestamp': '2026-09-21 10:00:00',
            'base_currency': 'USD',
            'target_currency': 'ZAR'
        }

        result = transformer.get_clean_rate(invalid_rate)
        assert result is None

    def test_clean_rate_data_missing(self, transformer):
        """ Test that checks cleaning of dat with missing fields. """
        missing_currency = {
            'rate': 18.5,
            'timestamp': '2026-09-21 10:00:00',
            # base and target currency missing here!
        }
        result = transformer.clean_rate_data(missing_currency)
        assert result is None

    def test_clean_rate_data_invalid_currency(self, transformer):
        """ Test cleaning data with invalid currency."""
        invalid_currency = {
            'rate': 18.5,
            'timestamp': '2026-09-21 10:00:00',
            'base_currency': 'XXX',
            'target_currency': 'ZAR'
        }

        result = transformer.clean_rate_data(invalid_currency)
        assert result is None

    def test_clean_rate_data_case_insensitive(self, transformer):
        """ Test that currency code are case-sensitive. """
        case_sensitive_data = {
            'rate': 18.5,
            'timestamp': '2026-09-21 10:00:00',
            'base_currency': 'usd',
            'target_currency': 'zar'
        }

        result = transformer.clean_rate_data(case_sensitive_data)
        assert result is not None
        assert result['base_currency'] == "USD"
        assert result['target_currency'] == 'ZAR'

    def test_transform_to_dataframe(self, transformer):
        """ Test tranforming the list of dictionaries to a DataFrame."""
        data_list = [
            {
                'rate': 18.5,
                'timestamp': '2026-09-21 10:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {
                
                'rate': 18.6,
                'timestamp': '2026-09-21 11:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {

                'rate': 18.4,
                'timestamp': '2026-09-21 12:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            }
        ]
        dataframe = transformer.transform_to_dataframe(data_list)

        assert isinstance(dataframe, pd.DataFrame)
        assert len(dataframe) == 2
        assert 'rate' in dataframe.columns
        assert 'timestamp' in dataframe.columns

    def test_transform_to_dataframe_empty(self, transformer):
        """ Test transformation of empty list to DataFrame. """
        df = transformer.transform_to_dataframe([])

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0


    def test_add_moving_average(self, transformer):
        """ Test that checks for adding moving average to DataFrame. """
        data_list = [
            {
                'rate': 18.5,
                'timestamp': '2026-09-21 10:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {
                'rate': 18.6,
                'timestamp': '2026-09-21 11:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {
                'rate': 18.4,
                'timestamp': '2026-09-21 12:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            }
        ]
        df = transformer.transform_to_database(data_list)
        df = transformer.add_moving_average(df, window=2)
        
    def test_add_rate_change(self, transformer):
        """ Test that checks adding rate change to DataFrame. """
        pass

    def test_detect_outliers(self, transformer):
        """ Test the outlier detection in DataFrame. """
        pass

    def test_aggregate_data(self, transformer):
        """ Test that checks data aggregation by time period. """
        pass

    def test_validate_data_quality(self, transformer):
        """ Test that checks for the data quality. """
        pass

if __name__ == "__main__":
    pytest.main([__file__, "-v"])