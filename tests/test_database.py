"""
Tests for the Database Storage Module
These tests verify that the database operations work correctly.
"""

import pytest
import tempfile
import os
from src.database.storage import CurrencyDatabase



class TestCurrencyDatabase:
    """ Test class for the CurrencyDatabase."""

    @pytest.fixture
    def temporary_db(self):
        """ Creates a temporary database for testing."""

        # Create a file that will be used for the database in the test.
        with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as temp_file:
            db_path = temp_file.name

        # This creates a database instance:
        db = CurrencyDatabase(db_path)

        yield db

        # Clean up process: closes the connection and deletes the temporary file.
        db.close()
        if os.path.exists(db_path):
            os.remove(db_path)

    def test_database_initialization(self, temp_db):
        """ Checks if the database can be initialized."""
        assert temp_db != None
        assert temp_db.connection != None
        assert temp_db.db_path.endswith('.db')

    def test_insert_rate(self, temp_db):
        """ Test to check when single rate is added into the database."""
        test_data = {
            'rate': 18.5,
            'timestamp': '2026-09-21 12:00:00',
            'base_currency': 'USD',
            'target_currency': 'ZAR'
        }

        result = temp_db.insert_rate(test_data)
        assert result == True

    def test_insert_rate_with_invalid_data(self, temp_db):
        """ Test data that is invalid."""
        invalid_data = {
            'rate': -1,         # invalid data
            'timestamp': '2026-09-21 12:00:00',
            'base_currency': 'USD',
            'target_currency': 'ZAR'
        }

        # The invalid data should still be inserted as the database does not validate.
        # The transformation must catch this.
        result = temp_db.insert_rate(invalid_data)
        assert result is True

    def test_insert_rates_multiple(self, temp_db):
        """ Test inserting multiple currency rates in a batch."""
        test_data = [
            { 
                'rate': 18.5,
                'timestamp': '2024-01-15 10:30:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR'
        },
        {
                'rate': 18.6,
                'timestamp': '2024-01-15 11:30:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR'
        },
       {
                'rate': 18.4,
                'timestamp': '2024-01-15 12:30:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR'
        }
        ]

        result = temp_db.insert_rates_multiple(test_data)
        assert result == 3

    def test_interest_rates_multiple_empty(self, temp_db):
        """ Test that checks if empty data is inserted."""
        result = temp_db.insert_rates_multiple ([])  
        assert result == 0                                                                                                                                                                                                                                        

    def test_get_latest_rates(self, temp_db):
        """ Test to see if latest currency is located in datbase."""
        # Test data to be used:
        test_data = [
            {
                'rate': 18.5,
                'timestamp': '2026-09-22 10:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {
                'rate': 18.6,
                'timestamp': '2026-09-22 11:30:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            }
        ]

        temp_db.insert_rates_multiple(test_data)

        # Get latest rates:
        latest = temp_db.get_latest_rates(limit=5)

        assert isinstance(latest, list)
        assert len(latest) >= 2

        # Check the structure to see if theres a rate, timestamp in the dictionary:
        for t_data in latest:
            assert isinstance(t_data, dict)
            assert 'rate' in latest
            assert 'timestamp' in latest
            assert 'base_currency' in latest
            assert 'target_currency' in latest

    def test_get_rates_by_date_range(self, temp_db):
        """ Test to check currency rates per date range."""
        # Data used for testing:
        test_data = [
           {
                'rate': 18.5,
                'timestamp': '2026-09-01 10:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {
                'rate': 18.6,
                'timestamp': '2026-09-08 11:30:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            }
        ]
        temp_db.insert_rates_multiple(test_data)

        # Get data by date range:
        rates = temp_db.get_rates_by_date_range('2026-09-01', '2026-09-08')

        assert isinstance(rates, list)
        # data should be returned within a range (1 week or more.)

    def test_get_statistics(self, temp_db):
        """ Test getting the stats for the database. """
        # Test data to be used:
        test_data = [
            {
                'rate': 18.5,
                'timestamp': '2026-09-22 10:00:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            },
            {
                'rate': 18.6,
                'timestamp': '2026-09-22 11:30:00',
                'base_currency': 'USD',
                'target_currency': 'ZAR',
            }
        ]

        temp_db.insert_rates_multiple(test_data)

        # Get the statistics from the database:
        stats = temp_db.get_statistics()

        assert isinstance(stats, dict)
        assert 'total_records' in stats
        assert 'min_rate' in stats
        assert 'max_rate' in stats
        assert 'avg_rate' in stats
        assert stats['total_records'] >= 2

    def test_database_close_connection(self, temp_db):
        """ Test that checks if the datbase connection closes. """
        assert temp_db.connection is not None

        # The close method should close the database connection without errors. 
        temp_db.close()
if __name__ == '__main__':
    pytest.main([__file__, "-v"])