# Import necessary libraries
import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    """
    This function fetches content from the given URL (Wikipedia's page on best-selling books)
    and prints out book titles and their approximate sales figures.
    
    Args:
    url (str): URL of the Wikipedia page to scrape.
    """
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Webpage fetched successfully!")
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first table on the page which contains the books
        table = soup.find('table', {'class': 'wikitable sortable'})
        
        # Extract rows from the table
        rows = table.find_all('tr')
        
        # Skip the header row and iterate through the rest
        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) > 1:  # Check if row has enough cells
                title = cells[0].text.strip()
                sales = cells[1].text.strip()
                print(f"Title: {title}, Sales: {sales}")
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# URL of the Wikipedia page on best-selling books
url = 'https://en.wikipedia.org/wiki/List_of_best-selling_books'

# Call the scrape function
scrape_books(url)
