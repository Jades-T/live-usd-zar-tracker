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

        # Email configuration:
        # self.send_message_server = os.getenv

        # Dashboard Configuration:
        self.dashboard_port = int(os.getenv('DASHBOARD_PORT', '8501'))
        self.dashboard_host = os.getenv('DASHBOARD_HOST', 'localhost')

        # Report Configiration:
        self.reports_dir = os.getenv('REPORTS_DIR', 'reports')
        self.logs_dir = os.getenv('LOGS_DIR', 'logs')

        # Automation configuration:
        self.auto_refresh_minutes = int(os.getenv('AUTO_REFRESH_MINUTES', '60'))
        self.enable_email_alerts = os.getenv('ENABLE_EMAIL_ALERTS', 'false').lower() == 'true'


    def get_database_path(self) -> str:
        """ 
        Gets the database path.
        
        Returns:
            Path to the SQLite database file.
        """
        return self.database_path


