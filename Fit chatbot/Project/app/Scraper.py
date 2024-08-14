import requests
from bs4 import BeautifulSoup

def scrape_and_save(url):
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        title_element = soup.find('div', class_='mt-0 mb-4').find('p', class_='lead')
        title = title_element.text.strip() if title_element else 'Title not found'

        content_elements = soup.find_all(lambda tag: tag.name in ['div', 'p'] and tag.get('style') == 'text-align: justify;')
        content = '\n\n'.join([element.text.strip() for element in content_elements]) if content_elements else 'Content not found'
        data = f"Title: {title}\n\nContent:\n{content}"

        with open('./data.txt', 'w', errors='ignore') as file:
            file.write(data)
        return "Successfully scraped data", 200
    except Exception as e:
        return str(e), 500