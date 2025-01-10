

https://github.com/user-attachments/assets/dfe8f8fe-2598-4fcc-a560-3c112357a2de






# Yallakora - Football Match Scraper

A Python web scraper that retrieves football match details from Yallakora based on a user-provided date (MM/DD/YYYY). The scraper extracts tournament name, teams, scores, and match time, then saves the data in a CSV file. It uses the `requests` and `BeautifulSoup` libraries for web scraping.

## Features
- Retrieves football match details from Yallakora.
- Extracts tournament name, teams, scores, and match time.
- Saves the data in a CSV file for easy access.
- User can provide the date in MM/DD/YYYY format to fetch relevant data.
- Uses Python libraries: `requests` and `BeautifulSoup`.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohamed-osamaaa/Yallakora.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Yallakora
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script by providing the date in MM/DD/YYYY format:

   ```bash
   python scraper.py MM/DD/YYYY
   ```

2. The match details for the given date will be extracted and saved to a CSV file in the project directory.

## Example

For example, to scrape matches for 01/10/2025, you would run:

```bash
python scraper.py 01/10/2025
```

This will create a CSV file `matches-details.csv` containing the extracted match details.

