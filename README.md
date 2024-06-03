
# Request
<img width="1152" alt="Screenshot 2024-06-03 at 10 10 22" src="https://github.com/Tobey/compare-api/assets/19887805/843a4e6c-2de0-4119-9ec0-861adb36dae1">

# Response

```json
{
    "matches": 13,
    "total": 20,
    "results": [
        {
            "field": "Net Income (in millions)",
            "source": 150,
            "database": 150,
            "match": true
        },
        {
            "field": "EBITDA (in millions)",
            "source": 400,
            "database": 400,
            "match": true
        },
        {
            "field": "ROE (Return on Equity) (%)",
            "source": 20,
            "database": 20.0,
            "match": true
        },
        {
            "field": "CEO",
            "source": "Alice Brown",
            "database": null,
            "match": false
        },
        {
            "field": "Location",
            "source": "Boston, MA",
            "database": "Boston",
            "match": false
        },
        {
            "field": "Debt (in millions)",
            "source": 300,
            "database": 300,
            "match": true
        },
        {
            "field": "Revenue Growth Rate (%)",
            "source": 15,
            "database": 15,
            "match": true
        },
        {
            "field": "Equity (in millions)",
            "source": 1000,
            "database": 1000,
            "match": true
        },
        {
            "field": "Industry",
            "source": "Financial Services",
            "database": "Financial Services",
            "match": true
        },
        {
            "field": "EBITDA Margin (%)",
            "source": 33.33,
            "database": 33.33,
            "match": true
        },
        {
            "field": "Number of Employees",
            "source": 1500,
            "database": null,
            "match": false
        },
        {
            "field": "Net Income Margin (%)",
            "source": null,
            "database": 12.5,
            "match": false
        },
        {
            "field": "Current Ratio",
            "source": 3,
            "database": 3.0,
            "match": true
        },
        {
            "field": "Enterprise Value (in millions)",
            "source": 4400,
            "database": 4300,
            "match": false
        },
        {
            "field": "ROA (Return on Assets) (%)",
            "source": 12,
            "database": 12.0,
            "match": true
        },
        {
            "field": "Debt to Equity Ratio",
            "source": 0.3,
            "database": 0.3,
            "match": true
        },
        {
            "field": "Market Capitalization",
            "source": 4500,
            "database": 4000,
            "match": false
        },
        {
            "field": "Company Name",
            "source": "FinanceLLC",
            "database": null,
            "match": false
        },
        {
            "field": "P/E Ratio",
            "source": 18,
            "database": 18,
            "match": true
        },
        {
            "field": "Revenue (in millions)",
            "source": 1200,
            "database": 1200,
            "match": true
        }
    ]
}

```
# Data discrepancy checker

This task mirrors a system we recently built internally, and will give you an
idea of the problems we need to solve.

Every quarter, new company data is provided to us in PDF format. We need to use
an external service to extract this data from the PDF, and then validate it
against data we have on file from another source.

Complete the API so that:

A user can provide a PDF and a company name data is extracted from the PDF via
the external service and compared to the data stored on file a summary of the
data is returned, containing all fields from both sources, noting which fields
did not match.

A selection of example PDFs have been uploaded, and the PDF
extraction service has been mocked for use in `src/pdf_service.py` - DO NOT
EDIT THIS FILE. There is simple documentation of the service in
`PDF_SERVICE_DOCS.md`. You can treat this as just another microservice.

The existing data we have on file is available in the `data/database.csv` file.

Treat this code as if it will be deployed to production, following best
practices where possible.

## Setup using Poetry

The easiest way to set up the repository is to use `python-poetry`. The lock file
was generated using version `1.8.3`

1. Ensure `poetry` is installed
2. Run `make install`

## Setup without Poetry

Alternatively it's possible to `pip install` directly using the
`pyproject.toml` or `requirements.txt`.
