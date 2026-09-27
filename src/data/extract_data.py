"""
Data Extraction Module
This module handles fetching USD/ZAR exchange rates from external API.
It's the first step in the data engineering pipeline: Extract.
"""

import requests
import json
import random
from datetime import datetime, timedelta

class CurrencyExtractor:
    """
    A class to extract USD/ZAR exchange rate data from APIs.
    This is the 'Extract' part of ETL (Extract, Transform, Load).
    """
    def __init__(self, base_url) -> None:
        """ This initializes the CurrencyExtractor."""

        # Use Free API, for simplicity: no authentication needed.

        self.base_url = base_url or "https://api.exchangerate-api.com/v4/latest/USD"

    def get_current_rate(self) -> dict:
        """ 
        Fetches the current USD/ZAR exchange rate from the API.

        Returns:
            Dict: that contains the exchange rate data / SHould return None if API fails.
            Example: {'rate': 18.5, 'timestamp': '2026-09-27 10:30:00'}
        """
        try:
            # Make request to the API
            response = requests.get(self.base_url, timeout=10)

            # Check if request was good.
            if response.status_code == 200:
                data = response.json()

                # Extract the ZAR rate from the API response.
                zar_rate = data.get('rates', {}).get('ZAR')

                if zar_rate:
                    result = {
                        'rate': zar_rate,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'base_currency': 'USD',
                        'target_currency': 'ZAR'
                    }
                    return result
                elif zar_rate is None:
                    print('ZAR rate not found in API response.')
                else:
                    print(f"API request failed with status code: {response.status_code}")
        except requests.exceptions.RequestException as error:
            print(f"Error fetching data from API: {error}")
        except json.JSONDecodeError as error:
            print(f"There was an error parsing the JSON response: {error}")    
