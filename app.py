import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from urllib.parse import urlparse, urljoin
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    return webdriver.Chrome(service=service, options=options)

def ensure_scheme(url):
    parsed = urlparse(url)
    if not parsed.scheme:
        return f"https://{url}"
    return url

def get_hyperlinks(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        anchor_text = link.get_text(strip=True)
        if not href.startswith(('http', 'https')):
            href = urljoin(base_url, href)
        links.add((href, anchor_text))
    return links

def check_link_status(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code >= 400:
            response = requests.get(url)  # Retry with GET if HEAD fails
        return response.status_code
    except requests.exceptions.RequestException:
        return None

def audit_links(links):
    return {url[0]: (check_link_status(url[0]), url[1]) for url in links}

def create_report(links_status, report_name):
    data = {
        'Link': [url for url in links_status.keys()],
        'Status': [info[0] for info in links_status.values()],
        'Link Text': [info[1] for info in links_status.values()]
    }
    df = pd.DataFrame(data)
    df.to_csv(f'{report_name}.csv', index=False)
    print(f"Audit complete. Report generated as '{report_name}.csv'.")

def single_page_audit(page_url):
    driver = setup_driver()
    driver.get(page_url)
    time.sleep(3)  # Let the page fully load
    links = get_hyperlinks(driver.page_source, page_url)
    driver.quit()
    links_status = audit_links(links)
    create_report(links_status, 'single_page_audit')

def run_audit():
    url = input("Enter the URL to audit: ")
    url = ensure_scheme(url)
    single_page_audit(url)

if __name__ == "__main__":
    run_audit()
