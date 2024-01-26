'''
This is a script to fetch data from a URL and write it to a file.
There are 4 types of data being used: Text, Excel, CSV, and JSON.
In the main function will be the folder_name, filename, and url to store each data file.
For every data file, there will be a quick statistical analysis that will be recored as a text file.
'''

# python standard library imports
import csv
import json
from pathlib import Path
import re
import math
import statistics

# import from virtual environment
import requests
import logging
import pandas as pd
import numpy as np

# local module imports
import shellenberger_utils as utils
import shellenberger_projsetup as projsetup

# Defining all the functions
    
def fetch_and_write_txt_data(folder_name:str, filename: str, url: str):
    '''
    Fetchs text data from a URL and writes it to a file.
    Displays different exceptions if an error is encountered.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    try:
        response = requests.get(url) # retrieves data from url text
        response.raise_for_status()
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text.lower())
            print(f"Text data saved to {file_path}")
    
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

def process_txt_data(folder_name: str, filename: str, results):
    '''
    Processes the data.txt file and outputs a txt file that is a word counter.
    :param folder_name: Name of the folder to find the file
    :param filename: Name of the file to open
    :param results: Name of the file to save the statistical analysis to
    '''
    with open(Path(folder_name).joinpath(filename), 'r') as file:
        raw_words = file.read().split() # splits text into strings
    words = [] # Empty list to store words without non-word characters
    for word in raw_words:
        word = re.sub('[,()?.\";!-]', '', word) # removes non-word characters from each word
        word = word.lower() # converts each word to lowercase
        words.append(word)
        unique_words = set(words) # set to store unique words
    with open(Path(folder_name).joinpath(results), 'w') as file:
        file.write(f"Unique words: {len(unique_words)}\n")
        for word in unique_words:
            file.write(f"The word {word} appears {words.count(word)} times.\n")
    
def fetch_and_write_excel_data(folder_name: str, filename: str, url: str):
    '''
    Fetchs Excel data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url Excel
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Excel data saved to {file_path}")
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def process_excel_data(folder_name: str, filename: str, results: str):
    '''
    Processes the Excel data for descriptions
    :param folder_name: Name of the folder to find the file
    :param filename: Name of the file to open
    :param results: Name of the file to save the statistical analysis to
    '''
    excel_data_df = pd.read_excel(Path(folder_name).joinpath(filename))
    excel_data_df.player_age = excel_data_df.player_age.astype(int)
    
    with open(Path(folder_name).joinpath(results), 'w') as file:
        file.write(f'2019 Player Age Description: \n'
                   f'{excel_data_df.player_age.describe()}')

def fetch_and_write_csv_data(folder_name: str, filename: str, url: str):
    '''
    Fetchs CSV data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
            print(f"CSV data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def process_csv_data(folder_name: str, filename: str, results: str):
    '''
    Processes the data.csv file and outputs a txt file that is a counter.
    :param folder_name: Name of the folder to find the file
    :param filename: Name of the file to open
    :param results: Name of the file to save the statistical analysis to
    '''
    with open(Path(folder_name).joinpath(filename), 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter= ',')
        headers = next(reader) # skip header
        
        total_rows = 0
        states = {}
        
        for row in reader:
            total_rows += 1
            if row[4] in states:
                states[row[4]] += 1
            else:
                states[row[4]] = 1
        with open(Path(folder_name).joinpath(results), 'w') as file:
            file.write(f"Total Stadiums: {total_rows}\n")
            for state, count in states.items():
                file.write(f"The state {state} has {round((count/total_rows) * 100, 1)}% of the total statdiums.\n")

def fetch_and_write_json_data(folder_name: str, filename: str, url: str):
    '''
    Fetchs JSON data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        Path(folder_name).mkdir(parents=True, exist_ok=True) # create folder if it doesn't
        file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
        with file_path.open('w') as file:
            file.write(response.text)
            print(f"JSON data saved to {file_path}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def process_json_data(folder_name: str, filename: str, results: str):
    
    with open(Path(folder_name).joinpath(filename), 'r') as file:
        stadium_data = dict(json.load(file))
    
    stadium_data['AverageDistance'] = []
    for value in stadium_data['DistanceMatrix']:
        stadium_data['AverageDistance'].append(round(sum(value)/(len(value) - 1), 2))
    
    count = 0
    with open(Path(folder_name).joinpath(results), 'w') as file:
        for stadium in stadium_data['Stadiums']:
            file.write(f"{stadium} is on average {stadium_data['AverageDistance'][count]} miles away from any other stadium.\n")
            count += 1
        
        


def main():
    '''
    Main function
    '''
    #print(f"Name:  {utils.company_name}")
    
    url_text = "https://storage.googleapis.com/kagglesdsdata/datasets/463494/941394/Shakespeare_01.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240124%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240124T015418Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5d0da122a3e4c7a356b8d4940847e96cc92e695cbd330044d29cc7a752d7810001753662bacdf25b21bfe4d0d3ff633a4b8f3f1ef23bd68afbdbecaa210e4b5f6c6a4614b940fcdc0beded8079a2829c3c38d860b46080222d9262db2f0f1954678287bcbafdf881e757ac9c106c1f271e63859ee5a790d3efa4a678933f11905932e44d61107699118e2bec17cdc8126c8437d422e7239000b9a32c66ee2ad253122c4be55e0ad73265a4fc55b6a3d453ab4bf1e2b82a55b1379bf33818a2cea0acf439669257e3058c7193047714e74a196efeb2eff7fddbed73a14dd22ba99f029f0dca5f55db2796fec7b6e67f33786af37d1781769f75946bc9f791323e"
    url_excel = "https://github.com/mikeygman11/Baseball-Statistics/raw/master/2019mlb.xlsx"
    url_csv = "https://query.data.world/s/352fjx2iiw5427wzmelxeky6fql6uh?dws=00000"
    url_json = "https://storage.googleapis.com/kagglesdsdata/datasets/496274/945103/StadiumsFull.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240124%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240124T021508Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=71e775d54b626f4f795aeebb70198e1dad862cb099ea8401a2c8657c507a3040d847a2288ba19b9d37adc9183e978c993c7cf4f7c355ca633c08dcd0d8fa655dc37b8b82a3cf06c23aee21e0452af773f2b2d0fcf19465f682b63d3bb664c88a9ef121685bf163b8291150848dace19a7aa2ecc2507e401d18e81c316a7c7acd61a7ceecbfd3162058bdf3f6065bfc6154e59e7059e38da497d0e638398a34544eff4b32f3255cea82868fa9b3f5fe394abe6ba914489329451dafc667db827161905aa497fc971544cb2b4bf283c9c6e86c7c05bbdb02d00a4be86c127da101aad3a01c1ae6772a1d2518774a284b2b1da3dc3c8398770d749b3a000a348ba0"
    
    txt_folder_name = "data-txt"
    excel_folder_name = "data-excel"
    csv_folder_name = "data-csv"
    json_folder_name = "data-json"
    
    txt_filename = 'data.txt'
    excel_filename = 'data.xls'
    csv_filename = 'data.csv'
    json_filename = 'data.json'
    
    #fetch_and_write_txt_data(txt_folder_name, txt_filename, url_text)
    #fetch_and_write_excel_data(excel_folder_name, excel_filename, url_excel)
    #fetch_and_write_csv_data(csv_folder_name, csv_filename, url_csv)
    #fetch_and_write_json_data(json_folder_name, json_filename, url_json)

    #process_txt_data(txt_folder_name, txt_filename, 'results_txt.txt')
    #process_excel_data(excel_folder_name, excel_filename, 'results_excel.txt')
    #process_csv_data(csv_folder_name, csv_filename, 'results_csv.txt')
    process_json_data(json_folder_name, json_filename, 'results_json.txt')


# conditional execution
if __name__ == "__main__":
    main()