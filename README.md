
# Webpage Link Auditor

## Overview
This Python script is designed to audit hyperlinks on a given webpage. It checks each hyperlink for its HTTP status code to determine if the link is active or broken. The script uses a combination of `requests`, `BeautifulSoup`, and `selenium` to fetch and parse webpage content, extract hyperlinks, and then check the status of each link. A report is generated in CSV format listing the URLs, their HTTP status codes, and the anchor text.

## Features
- **Automated Browser Interaction**: Uses Selenium WebDriver to handle webpages that require JavaScript rendering.
- **Link Extraction**: Parses HTML content to extract all hyperlinks and ensures they are absolute URLs.
- **Status Check**: Checks each hyperlink's status using HTTP methods to identify broken links.
- **Report Generation**: Outputs a CSV file with the link, HTTP status, and the link text for review.

## Installation

### Prerequisites
Ensure you have Python installed on your system. This script has been tested with Python 3.9. You also need pip for installing Python packages. The script requires an internet connection for fetching webpage content and downloading the Chrome WebDriver automatically.

### Required Python Packages
This project uses several external Python libraries. You can install them using pip:

\```bash
pip install requests beautifulsoup4 selenium webdriver-manager pandas
\```

### Setting Up Selenium WebDriver
The script uses `ChromeDriverManager` from `webdriver-manager`, which simplifies the management of binary drivers for different browsers. This setup ensures that you always have the latest compatible version of ChromeDriver installed automatically.

## Running the Script

To run the script, follow these steps:

1. Open your command line interface (CLI).
2. Navigate to the directory containing the script.
3. Run the script by typing:

\```bash
python app.py
\```

4. When prompted, enter the URL you want to audit. Ensure the URL is entered correctly to avoid errors during the audit process.

## Output
After executing, the script will generate a CSV report named `single_page_audit.csv` in the same directory as the script. This report contains columns for the link, the HTTP status code, and the link text.

## Limitations
- The script currently only audits links on the page initially loaded. It does not follow links to subsequent pages or handle pagination.
- JavaScript heavy sites may require additional sleep time to ensure all elements are fully loaded before link extraction.

## Contribution
Feel free to fork this repository and contribute by refining the script or adding new features. Your contributions are much appreciated!
