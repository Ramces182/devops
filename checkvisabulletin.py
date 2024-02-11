import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Function to extract filing date from the given HTML content and row index
def extract_filing_date(html_content, row_index):
    soup = BeautifulSoup(html_content, 'html.parser')
    family_table = None
    for table in soup.find_all('table'):
        if 'family' in table.text.lower():
            family_table = table
            break

    if family_table:
        for i, row in enumerate(family_table.find_all('tr')):
            if i == row_index:
                file_date_cell = row.find_all('td')[4]
                return file_date_cell.text.strip()

    return None

# Get the current month and year
current_date = datetime.now()

# Iterate over the last 4 months including the current month
for i in range(4, 0, -1):
    # Get the month and year in lowercase for constructing the URL
    check_month_year = current_date.strftime('%B-%Y').lower()

    # Construct the URL based on the current month and year
    url = f"https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin/2024/visa-bulletin-for-{check_month_year}.html"

    # Fetch HTML content
    response = requests.get(url)
    html_content = response.text

    # Extract the filing date for F4 Mexico (5th column, 6th row)
    file_date = extract_filing_date(html_content, 5)

    # Print the extracted filing date and the current date
    print(f"F4 Mexico Filing Date for {check_month_year}: {file_date}")
    print(f"Current Date: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    print('-' * 30)
