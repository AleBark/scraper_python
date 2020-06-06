# -*- coding: utf-8 -*-
from scraper.models.HtmlHandler import HtmlHandler
from bs4 import BeautifulSoup

"""
Ale Bark Bruneri
"""


def main():
    html_handler = HtmlHandler("https://pixabay.com/pt/images/search/")
    html = html_handler.get_html()

    soup = BeautifulSoup(html, 'html.parser')
    div_items = soup.find('div', attrs={'class': 'search_results'})
    total_images = len(list(div_items.children))

    print("Total de imagens:" + str(total_images))
    print("")
    print("Top 5 downloads:")

    # Sim, isso é terrível de feio
    cont = 0

    if total_images > 0:
        for item in div_items.find_all('img'):
            if cont >= 5:
                return
            print("Descrição: " + item.attrs['alt'])
            print("Links: " + item.attrs['srcset'])
            print("")
            cont = cont + 1


if __name__ == '__main__':
    main()
