"""
Pytest configuration file
This file sets up the test environment and fixtures.
"""
import sys
import os

# add the src dir to the Python path:
src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)