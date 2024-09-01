import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
from management import execute_command_line
import sys
import datetime
from pathlib import Path

SUPPORTED_FORMATS = {"json", "csv"}


def main():
    try:
        file_path, url, format = execute_command_line()

        if not format:
            format = "json"

        format = format.lower()
        if format not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported format {format}. Supported formats are {','.join(SUPPORTED_FORMATS)}")

        if not file_path:
            file_path = str(Path.cwd() / str(datetime.datetime.now())) + f".{format}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(class_='codes')
        rows = results.find_all('tr')
        categories = []
        category_row = []
        # extract texts from results
        for row in rows:
            table_row_list = row.find_all('td')
            category_row = []
            for table_row in table_row_list:
                category_row.append(table_row.text.strip())
            categories.append(category_row)

        save_data_to_file(categories, format, file_path)

    except requests.exceptions.MissingSchema as exc:
        sys.stderr.write("\nInvalid URL '{}' Did you mean 'https://{}'?.\n".format(url, url))
        sys.exit(1)


def save_data_to_file(data, format, file_path):
    header, rows = data[0], data[1:]
    df = pd.DataFrame(rows, columns=header)
    if format == "json":
        json_data = df.to_dict(orient='records')
        # Save to JSON file
        with open(file_path,
                  'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    if format == "csv":
        df.to_csv(file_path, encoding='utf-8')


if __name__ == '__main__':
    main()
