
# Variables:
PYTHON := python3
PIP := pip3
PROJECT_NAME := live-usd-zar-Tracker

BLUE := \033[0;34m
GREEN := \033[0;32m
RED := \033[0;31m

NC := \033[0m # No Color

help:
	@echo "$(BLUE)LIVE USD ZAR TRACKER - Available Commands:$(NC)"
	@echo ""
	@echo "$(GREEN)Development Commands:$(NC)"
	@echo "  make install       - Install Python dependencies"
	@echo "  make test          - Run pytest tests"
	@echo "  make test-verbose  - Run tests with verbose output"

# Install dependencies
install:
	@echo "$(BLUE)Installing Project / Python dependencies ...$(NC)"
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)Dependencies installed successfully!$(NC)"
	

# Run tests
test:
	@echo "$(BLUE)Running tests...$(NC)"
	$(PYTHON) -m pytest tests/ -v
	@echo "$(GREEN)Tests completed!$(NC)"


# Run tests with verbose output
test-verbose:
	@echo "$(BLUE)Running tests with verbose output...$(NC)"
	$(PYTHON) -m pytest tests/ -vv --tb=short
	@echo "$(GREEN)Test completed!$(NC)"
	