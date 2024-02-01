from bs4 import BeautifulSoup


def get_code(text):
    
    soup = BeautifulSoup(text, 'html.parser')
    Strongs = soup.find_all('strong')
    for strong in Strongs:
        if len(strong.text)==6: 
            return strong.text