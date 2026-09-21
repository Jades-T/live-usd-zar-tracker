"""
Tests for the Database Storage Module
These tests verify that the database operations work correctly.
"""

import pytest
import tempfile
import os
from src.database.storage import CurrencyDatabase



class TestCurrencyDatabase:
    """
    Test class for the CurrencyDatabase.
    """

    @pytest.fixture
    def temporary_db(self):
        """
        Creates a temporary database for testing
        """

        # Create a file that will be used for the database in the test.
        with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as temp_file:
            db_path = temp_file.name

        # This creates a database instance:
        db = CurrencyDatabase(db_path)

        # Clean up process: closes the connection and deletes the temporary file.
        