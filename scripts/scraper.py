import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.jdpower.com/'

def fetch_page(url, headers=None):
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()

        print(response.text)
        return response.text

    except requests.RequestException as e:
        print(f"Error fetching {url}, Error:", e)

def parse_html(html_content):
    """ Parse HTML content from Edmunds """
    return BeautifulSoup(html_content, 'html.parser')

def extract_data(soup):
    """
    * Car Year
    * Car Make
    * Car Model
    * Variant
    * Mileage
    * Body type
    * Original price
    * Current price
    * Engine fuel type
    """
    data = []

    pages = soup.find('div', class_='body-copy spacing-xs MuiBox-root mui-xi606m')
    pages = int(int(pages) / 23)

    for page in range(1, pages + 1):
        page_content = fetch_page(BASE_URL + 'inventory/srp.html?inventorytype=used' + f'?page={page}')
        page_soup = parse_html(page_content)

        container = page_soup.find('div', class_='undefined')

        listings = container.find_all('div', class_='srp_vehicle-card__sFMkN spacing-s track-srp-inventory-module')

        for car in listings:
            car_div = car.find('div', class_='srp_vehicle-detail-left__7P58C')

            href = car_div.find('a').get('href')

            car_detail_soup = parse_html(fetch_page(href))

            # This is where I stopped working because my scrapper wasn't fetching anything and giving me errors.

        
def main():
    url = BASE_URL + 'inventory/srp.html?inventorytype=used'  
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    html_content = fetch_page(url, headers=headers)
    if not html_content:
        return

    soup = parse_html(html_content)
    data = extract_data(soup)


    
    # Process and store data as needed (e.g., CSV, database)
    for record in data:
        print(record)
    

if __name__ == "__main__":
    main()
