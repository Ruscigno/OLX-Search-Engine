from bs4 import BeautifulSoup
import requests
import logging

def checkSellItem(tag):
    return tag.has_attr('data-list_id') and tag.has_attr('data-featured')

def getLinkFromAllItems(address, pageNumber=1):
    page = requests.get(address + '?o=' + str(pageNumber))
    soup = BeautifulSoup(page.content, "html.parser")
    #list_items = soup.find_all("li", {"class": "item"})
    list_items = soup.find_all(checkSellItem)
    for item in list_items:
