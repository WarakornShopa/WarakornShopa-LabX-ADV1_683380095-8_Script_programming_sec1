
# Lab 7 ADV: Advanced Web Scraping & Introduction to Automated Agents

## Project Overview

This project is an automated web scraper built with Python and Selenium.
It collects book information from Books to Scrape and saves the results
in a JSON file.

The scraper reads its settings from a JSON configuration file, visits
the website, extracts product information, navigates through multiple
pages, and saves the collected data.

## Features

- Configuration-driven web scraping
- Automated browser control using Selenium
- Extracts book names, prices, product URLs, and image URLs
- Supports pagination
- Configurable maximum number of pages
- Configurable delay between pages
- Exports scraped data to JSON

## Technologies Used

- Python
- Selenium
- BeautifulSoup4
- WebDriver Manager
- JSON

## Project Structure

```text
Lab07-ADV-Web-Scraping/
├── configs/
│   └── example_site_config.json
├── data/
│   └── scraped_products.json
├── docs/
│   └── ETHICS.md
├── src/
│   ├── __init__.py
│   ├── config_parser.py
│   ├── data_models.py
│   ├── driver_manager.py
│   ├── scraper_agent.py
│   └── utils.py
├── main.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or newer
- Google Chrome
- Internet connection

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows CMD:

   ```cmd
   .venv\Scripts\activate.bat
   ```

5. Install the required packages:

   ```bash
   python -m pip install selenium beautifulsoup4 webdriver-manager
   ```

## Configuration

Edit `configs/example_site_config.json` to change the starting URL,
maximum number of pages, delay, and CSS selectors.

The current configuration starts from the Books to Scrape book category,
scrapes up to 3 pages, and waits 2 seconds between pages.

## How to Run

Run the following command from the project root:

```bash
python main.py
```

The collected data will be saved to:

`data/scraped_products.json`

## Test Results

The scraper was run successfully against Books to Scrape.

- Pages scraped: 3
- Products collected: 60
- Output format: JSON

## Ethical Considerations

This project is for educational purposes.
Please respect website policies, avoid excessive requests, and collect
only the information necessary for the project.

See `docs/ETHICS.md` for more information.