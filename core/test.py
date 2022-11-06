import requests
from bs4 import BeautifulSoup


url = "https://www.iransporter.com/product/4079-127/%D8%B3%D8%AA-%DB%8C%D9%88%DA%AF%D8%A7-%D9%88-%D8%A8%D8%AF%D9%86%D8%B3%D8%A7%D8%B2%DB%8C-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A7%D8%B3%D9%BE%D9%88%D8%B1%D8%AA%D8%B1-i-s-fitnessset.aspx"

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')

price = content.find('span', class_='price')

print(price.contents[0])

