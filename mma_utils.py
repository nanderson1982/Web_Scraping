import requests
from bs4 import BeautifulSoup as bs
import psycopg2



def fetch_and_parse(url: str):
    """
    Purpose:
        Fetches a webpage from the specified URL and parses it into a BeautifulSoup object for HTML processing.

    Args:
        url (str): The URL of the webpage to fetch and parse.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the parsed HTML of the fetched webpage.

    Example:
        # Fetch and parse HTML from a webpage
        soup = fetch_and_parse("https://example.com/table-page")
    """
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    return soup



def get_table_body(soup: bs):
    """
    Purpose:
        Extracts the first table element from the provided BeautifulSoup object.

    Args:
        soup (BeautifulSoup OR bs): A BeautifulSoup object containing parsed HTML from which to extract the table.

    Returns:
        element.Tag: The first table element found in the BeautifulSoup object, if any.

    Example:
        # Assuming `soup` is a BeautifulSoup object obtained from fetch_and_parse
        table_body = get_table_body(soup)
    """
    table_body = soup.find('table')
    return table_body



def get_event_links(events_url: str):
    """
    Purpose:
        Extracts and compiles a list of URLs pointing to all completed UFC events from a given webpage.

    Args:
        events_completed_url (str): The URL of the webpage containing links to completed UFC events.

    Returns:
        List[str]: A list of URLs, each pointing to a completed UFC event.

    Example:
        # Assuming `events_completed_url` is the URL to a webpage listing completed UFC events
        events_url = "https://example.com/ufc-events"
        event_links = get_event_links(events_url)
        print(event_links)  # Outputs a list of URLs to completed UFC events
    """
    
    # Assuming get_table_body is defined elsewhere and returns a BeautifulSoup object
    soup = fetch_and_parse(events_url)
    
    table_body = soup.find('table')
    event_links = []

    # Iterate through each row in the table to find event links
    for row in table_body.find_all('tr'):
        cols = row.find_all('td')
        for col in cols:
            a_tag = col.find('a')  # Find the anchor tag
            if a_tag:  # Check if the anchor tag exists
                event = a_tag['href']  # Extract the href attribute (URL)
                event_links.append(event)
                
    return event_links




