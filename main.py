# -*- coding: utf-8 -*-
import time

from scraper.models.HtmlHandler import HtmlHandler
from bs4 import BeautifulSoup

"""
Ale Bark Bruneri
"""


def main():
    html_handler = HtmlHandler("https://startupbase.com.br/home/startups?q=&states=all&cities=all&segments=all&targets=all&phases=all&models=all&badges=all")
    html = html_handler.get_html()

    html_handler.maximize_window()
    html_handler.dismiss_popup('onesignal-popover-cancel-button')
    time.sleep(5)

    html_handler.scroll_page_down('/html/body/app-root/ng-component/app-layout/div/div/div/div/div/app-layout-column/ng-component')

    # soup = BeautifulSoup(html, 'html.parser')

if __name__ == '__main__':
    main()
