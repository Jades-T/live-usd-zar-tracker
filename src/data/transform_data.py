"""
This file handles the cleaning and transforming of raw data.
"""

import pandas as pd
from datetime import datetime
from typing import Dict

class DataTransformer:
    """
    Class that transforms and cleans the currency data.
    - Ensures the data has quality before used for analysis / viz.
    """

    def __init__(self) -> None:
        self.valid_currencies: list[str] = ['USD', 'ZAR', 'EUR', 'GBP']

    def clean_the_rate_data(self, raw_data) -> None:
        """
        Cleans and validates the single rate data point.
        Checks for missing values, invalid types.

        Args:
            - raw_data: Raw dictionary with rate information.

        Returns:
            - Cleaned dictionary / None if data is invalid.
        """
        if not raw_data:
            return None

        try:
            required_fields: list[str] = ['rate', 'timestamp', 'base_currency', 'target_currency']
            
            # Checks if the required data fields exists.
            for field in required_fields:
                if field not in raw_data:
                    print(f"Required field missing: {field}")
                    return None

            # Check that the rate is a -ve number.
            rate = float(raw_data['rate'])
            if rate <= 0 or rate >= 100:
                print(f"Invalid rate value: {rate}")
                return None

            # Check currencies are uppercase.
            base = raw_data['base_currency'].upper()
            target = raw_data['target_currency'].upper()

            if base and target not in self.valid_currencies:
                print(f"Invalid currency pairs: {base}/{target}")
                return None