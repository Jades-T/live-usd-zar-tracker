"""
This file handles the cofiguration settings for the project.
Looks at the config for loading env, database connection, API config, 
email config, dashboard, report and automation configuration.
"""

import os
from dotenv import load_dotenv

class Config:
    """ Class config manages the configuration settings for all phases of the lifecycle."""

    def __init__(self) -> None:
        """ This initializes the configuration by loading environment variables."""
        load_dotenv()

        # Database configuration:
        self.database_path = os.getenv("DATABASE_PATH", "currency_rates.db")

        # API configuration:
        self.api_base_url = os.getenv('API_BASE_URL', 'https://api.exchangerate-api.com/v4/latest/USD')
        self.api_timeout = int(os.getenv('API_TIMEOUT', '10'))