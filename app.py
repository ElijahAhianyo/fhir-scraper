import requests
from bs4 import BeautifulSoup
import pandas as pd
from management import execute_command_line
import sys




def main():
    try:
        file_path,url = execute_command_line() #get arguments(file path and url) from command line
        page = requests.get(url) 
        soup = BeautifulSoup(page.content,'html.parser')
        results = soup.find(class_='codes') 
        rows = results.find_all('tr')
        categories = []
        category_row = []
        # extract texts from results
        for row in rows: 
            table_row_list = row.find_all('td') 
            category_row = [] 
            for table_row in table_row_list: 
                category_row.append(table_row.text) 
            categories.append(category_row) 

        # convert results to dataframe and rite to specified file path
        dfobj = pd.DataFrame(categories) 

        dfobj.to_csv(file_path, encoding='utf-8')

    except requests.exceptions.MissingSchema as exc:
        sys.stderr.write("\nInvalid URL '{}' Did you mean 'https://{}'?.\n".format(url, url))
        sys.exit(1)


if __name__ == '__main__':
    main()