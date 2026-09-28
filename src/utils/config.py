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
        self.database_path: str = os.getenv("DATABASE_PATH", "currency_rates.db")

        # API configuration:
        self.api_base_url: str = os.getenv('API_BASE_URL', 'https://api.exchangerate-api.com/v4/latest/USD')
        self.api_timeout = int(os.getenv('API_TIMEOUT', '10'))

        # Email configuration:
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.sender_email = os.getenv('SENDER_EMAIL', '')
        self.sender_password = os.getenv('SENDER_PASSWORD', '')

        # Dashboard Configuration:
        self.dashboard_port = int(os.getenv('DASHBOARD_PORT', '8501'))
        self.dashboard_host: str = os.getenv('DASHBOARD_HOST', 'localhost')

        # Report Configiration:
        self.reports_dir: str = os.getenv('REPORTS_DIR', 'reports')
        self.logs_dir: str = os.getenv('LOGS_DIR', 'logs')

        # Automation configuration:
        self.auto_refresh_minutes = int(os.getenv('AUTO_REFRESH_MINUTES', '60'))
        self.enable_email_alerts: bool = os.getenv('ENABLE_EMAIL_ALERTS', 'false').lower() == 'true'


    def get_database_path(self) -> str:
        """ 
        Gets the database path.
        
        Returns:
            Path to the SQLite database file.
        """
        return self.database_path

    def is_email_configured(self) -> bool:
        """
        Checks if the email configuration is done.
        
        Returns:
            True if email credentials are configured, False if not.
        """
        return bool(self.sender_email and self.sender_password)

    def string_representation_config(self) -> str:
        """
        Displays the configuration.

        Returns:
            - config database path
            - api timeoit
            - email config.
        """
        return (f"Config(database_path: {self.database_path}, "
                f"api_time: {self.api_timeout}, "
                f"Email_configured: {self.is_email_configured()}")

# Global config instance:
config = Config()

if __name__ == "__main__":
    # Test the configuration:
    print("Testing the configuration:")
    print(f"Configuration: {config}")
    print(f"Database Path: {config.get_database_path()}")
    print(f"Email configuration: {config.is_email_configured()}")