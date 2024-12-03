import json
from bs4 import BeautifulSoup
import requests

def clean_country_name(name):
    # Remove text in parentheses and special notes
    if ('(' in name):
        name = name.split('(')[0]
    if ('officially' in name.lower()):
        name = name.split('officially')[0]
    
    # Remove specific terms
    remove_terms = [
        'not a country, but a state (an emirate) within the United Arab Emirates',
        '(French overseas department)',
        '(French overseas collectivity)',
        'unrecognised, self-declared state',
    ]
    for term in remove_terms:
        name = name.replace(term, '')
    
    return name.strip()

def get_driving_sides():
    url = "https://www.worldstandards.eu/cars/list-of-left-driving-countries/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the table with driving information
    table = soup.find('table', {'id': 'tablepress-3'})
    
    driving_sides = {}
    
    # Process each row in the table
    for row in table.find_all('tr')[1:]:  # Skip header row
        columns = row.find_all('td')
        if (len(columns) == 3):
            country = clean_country_name(columns[0].text)
            side = columns[2].text.strip()
            
            if (country and side):
                driving_sides[country] = side

    # Sort dictionary by keys
    driving_sides = dict(sorted(driving_sides.items()))
    
    # Save to JSON file
    with open('data/driving_side/countries_driving_side.json', 'w', encoding='utf-8') as f:
        json.dump(driving_sides, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    get_driving_sides()
