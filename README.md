# USD/ZAR Currency Tracker

A comprehensive data engineering project that demonstrates the complete lifecycle of data engineering: **Extract, Transform, Load (ETL)**, with automated reporting, visualization, and deployment.

## Project Overview

This project is a live USD/ZAR (US Dollar to South African Rand) currency tracker that:
- Fetches real-time exchange rates from external APIs
- Stores data in a SQLite database
- Transforms and cleans the data
- Visualizes data through an interactive web dashboard
- Generates automated PDF reports (daily, weekly, monthly)
- Sends email notifications with reports
- Includes comprehensive testing and CI/CD pipeline

## Tech Stack

- **Language**: Python 3.11
- **Database**: SQLite3
- **Dashboard**: Streamlit
- **Data Processing**: Pandas
- **API**: Requests
- **PDF Generation**: ReportLab
- **Testing**: Pytest
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Build Automation**: Make

## Project Structure

```
usd_zar_tracker/
├── src/
│   ├── data/
│   │   ├── extraction.py      # API data extraction
│   │   └── transformation.py  # Data cleaning and transformation
│   ├── database/
│   │   └── storage.py         # SQLite database operations
│   ├── visualization/
│   │   └── dashboard.py       # Streamlit web dashboard
│   ├── automation/
│   │   ├── reports.py         # PDF report generation
│   │   ├── email_sender.py    # Email automation
│   │   └── pipeline.py        # Complete ETL pipeline orchestration
│   └── utils/
│       └── config.py          # Configuration management
├── tests/
│   ├── test_extraction.py     # Tests for extraction module
│   ├── test_database.py       # Tests for database module
│   └── test_transformation.py # Tests for transformation module
├── reports/                   # Generated PDF reports
├── logs/                      # Application logs
├── .github/workflows/
│   └── ci-cd.yml            # CI/CD pipeline configuration
├── Dockerfile                 # Docker container definition
├── Makefile                   # Build automation commands
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Docker (optional, for containerization)
- Make (optional, for build automation)

### Local Installation

1. **Clone the repository** (or navigate to the project directory):
```bash
cd usd_zar_tracker
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

Or use the Makefile:
```bash
make install
```

3. **Set up environment variables** (optional, for email functionality):
```bash
cp .env.example .env
# Edit .env with your email credentials
```

### Docker Installation

1. **Build the Docker image**:
```bash
make docker-build
```

2. **Run the container**:
```bash
make docker-run
```

The dashboard will be available at `http://localhost:8501`

## Usage

### Running the Dashboard

Start the interactive web dashboard:

```bash
streamlit run src/visualization/dashboard.py
```

Or using Make:
```bash
make dashboard
```

### Running the ETL Pipeline

Execute the complete data pipeline:

```bash
python src/automation/pipeline.py
```

Or using Make:
```bash
make pipeline
```

### Loading Historical Data

Load sample historical data for testing:

```bash
make load-data
```

### Running Tests

Execute the test suite:

```bash
pytest tests/
```

Or using Make:
```bash
make test
```

### Available Make Commands

```bash
make help          # Show all available commands
make install       # Install Python dependencies
make test          # Run tests
make dashboard     # Start the dashboard
make pipeline      # Run ETL pipeline
make docker-build  # Build Docker image
make docker-run    # Run Docker container
make clean         # Clean generated files
```

## Data Engineering Concepts Demonstrated

### 1. **Extract (Data Extraction)**
- Fetching data from external APIs using the `requests` library
- Handling API errors and retries
- Working with JSON data formats
- Rate limiting and timeout handling

**Key File**: `src/data/extraction.py`

### 2. **Transform (Data Transformation)**
- Data cleaning and validation
- Handling missing or invalid data
- Data type conversion and standardization
- Calculating derived metrics (moving averages, rate changes)
- Outlier detection
- Data aggregation for reporting

**Key File**: `src/data/transformation.py`

### 3. **Load (Data Storage)**
- SQLite database design and schema creation
- CRUD operations (Create, Read, Update, Delete)
- Batch insertion for performance
- Data querying and filtering
- Database connection management

**Key File**: `src/database/storage.py`

### 4. **Visualization**
- Interactive web dashboards using Streamlit
- Real-time data visualization
- Chart creation and customization
- User interaction and filtering

**Key File**: `src/visualization/dashboard.py`

### 5. **Automation**
- Automated report generation (PDF)
- Email automation and notifications
- Scheduled task execution
- Pipeline orchestration

**Key Files**: `src/automation/reports.py`, `src/automation/email_sender.py`, `src/automation/pipeline.py`

### 6. **Testing**
- Unit testing with pytest
- Test fixtures and setup
- Mocking external dependencies
- Test coverage

**Key Files**: `tests/test_*.py`

### 7. **DevOps & Deployment**
- Containerization with Docker
- CI/CD pipeline with GitHub Actions
- Automated testing and deployment
- Build automation with Make

**Key Files**: `Dockerfile`, `.github/workflows/ci-cd.yml`, `Makefile`

## Features

### Real-time Dashboard
- Live USD/ZAR exchange rate tracking
- Historical data visualization
- Interactive charts and graphs
- Statistics and analytics
- Data quality indicators

### Automated Reports
- **Daily Reports**: Current rate, daily statistics, recent movements
- **Weekly Reports**: Weekly summary, daily breakdown, trends
- **Monthly Reports**: Monthly analysis, weekly summaries, volatility metrics

### Email Notifications
- Automated report delivery
- Configurable recipient lists
- Alert system for significant rate changes

### Data Quality
- Automatic data validation
- Outlier detection
- Missing data handling
- Data quality reports

## Testing

The project includes comprehensive unit tests for all major components:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_extraction.py

# Run with verbose output
pytest tests/ -vv
```

## Docker Usage

### Build the Image
```bash
docker build -t usd_zar_tracker .
```

### Run the Container
```bash
docker run -d -p 8501:8501 --name currency_tracker usd_zar_tracker
```

### Run Tests in Docker
```bash
docker run --rm usd_zar_tracker pytest tests/
```

### Stop and Clean
```bash
docker stop currency_tracker
docker rm currency_tracker
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Runs tests** on every push and pull request
2. **Performs code quality checks** (linting, formatting)
3. **Builds Docker images**
4. **Runs security scans**
5. **Deploys** on successful tests (main branch only)

### Workflow Triggers
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop`
- Manual trigger via GitHub Actions UI

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Database
DB_PATH=currency_rates.db

# API Configuration
API_BASE_URL=https://api.exchangerate-api.com/v4/latest/USD
API_TIMEOUT=10

# Email Configuration (optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password

# Dashboard Configuration
DASHBOARD_PORT=8501
DASHBOARD_HOST=localhost

# Automation
AUTO_REFRESH_MINUTES=60
ENABLE_EMAIL_ALERTS=false
```

## Learning Resources

This project demonstrates real-world data engineering concepts:

- **ETL Pipelines**: Extract, Transform, Load processes
- **Data Quality**: Validation, cleaning, and monitoring
- **Database Design**: Schema design and optimization
- **API Integration**: Working with external data sources
- **Automation**: Scheduled tasks and report generation
- **Visualization**: Making data accessible and understandable
- **Testing**: Ensuring code quality and reliability
- **DevOps**: Containerization and continuous integration

## Contributing

This is an educational project designed to help beginners understand data engineering concepts. Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is created for educational purposes.

## Acknowledgments

- Exchange rate data from [exchangerate-api.com](https://www.exchangerate-api.com/)
- Built with [Streamlit](https://streamlit.io/)
- Testing with [Pytest](https://pytest.org/)

## Support

For questions or issues, please refer to the inline code comments which are designed to be beginner-friendly and explain concepts in simple terms.

---

**Note**: This project is designed for educational purposes to demonstrate data engineering concepts. The exchange rate data is for demonstration only and should not be used for actual financial decisions.