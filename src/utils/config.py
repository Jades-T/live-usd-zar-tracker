"""
This file handles the cofiguration settings for the project.
Looks at the config for loading env, database connection, API config, 
email config, dashboard, report and automation configuration.
"""

import os
from dotenv import load_dotenv

class Config:
    """ Class config manages the configuration settings for all phases of the lifecycle."""

    