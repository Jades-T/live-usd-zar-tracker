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

        return self.base_url = base_url or "https://api.exchangerate-api.com/v4/latest/USD"

        