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

    def __init__(self):
        self.valid_currencies: list = ['USD', 'ZAR', 'EUR', 'GBP']

    def clean_the_rate_data(self, raw_data: dict):
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
            required_fields: list = ['rate', 'timestamp', 'base_currency', 'target_currency']
            
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

            # Clean timestamp data
            timestamp: str = self._clean_timestamp(raw_data['timestamp'])
            if not timestamp:
                return None

            cleaned_data = {
                'rate': round(rate, 4),
                'timestamp': timestamp,
                'base_currency': base,
                'target_currency': target
            }
            return cleaned_data
        
        except (ValueError, TypeError) as error:
            print(f"Error cleaning data: {error}")
            return None
    
    def _clean_timestamp(self, timestamp:str) ->  str:
        """ 
        Clean the timestamp format.

        Args:
            timestamp: raw timestamp string (not yet cleaned)

        Returns:
            Cleaned timestamp string of None if invalid.        
        """
        try:
            if isinstance(timestamp, str):
                # different format options:
                formats: list[str] = [
                    '%Y-%m%-%d% %H:%M:%S',
                    '%Y-%m-%d',
                    '%d/%m/%Y %H:%M:%S',
                    '%d/%m/%Y'
                ]

                for format in formats:
                    try:
                        dt: str = datetime.strftime(timestamp, format)
                        return dt.strftime('%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        continue
        except Exception as error: 
            print(f"Error clean timestamp: {error}")

    def transform_to_dataframe(self, data_list: list) -> pd.DataFrame:
        """
        Takes a list of dictionaries and creates a pandas Dataframe with it.

        Args:
            - data_list: List of dictionaries (rate data)

        Returns:
            - pandas Dataframe with data.
        """
        if not data_list:
            return pd.DataFrame()

        try:
            # converts the data_list to a dataframe.
            dataframe = pd.DataFrame(data_list)

            # Check for correct datatypes:
            dataframe['rate'] = pd.to_numeric(dataframe['rate'], errors='coerce')
            # errors='coerce' : tells pandas not to throw an error if it cant convert the list to dataframe.
