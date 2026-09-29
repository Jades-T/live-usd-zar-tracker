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
