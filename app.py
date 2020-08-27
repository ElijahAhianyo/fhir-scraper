import requests
from bs4 import BeautifulSoup
import pandas as import pdb




url = 'https://www.hl7.org/fhir/valueset-service-category.html'

page = requests.get(url) 

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find(class_='codes') 

rows = results.find_all('tr')

categories = []

category_row = []

for row in rows: 
    table_row_list = row.find_all('td') 
    category_row = [] 
    for table_row in table_row_list: 
        category_row.append(table_row.text) 
    categories.append(category_row) 


dfobj = pd.DataFrame(categories) 

dfobj.to_csv('health_cat.csv', encoding='utf-8')

