'''
This is a script to fetch data from a URL and write it to a file.
There are 4 types of data being used: Text, Excel, CSV, and JSON.
In the main function will be the folder_name, filename, and url to store each data file.
For every data file, there will be a quick statistical analysis that will be recored as a text file.
'''

# python standard library imports
import csv
from pathlib import Path

# import from virtual environment
import requests

# local module imports
import shellenberger_utils as utils
import shellenberger_projsetup as projsetup

# Defining all the functions

def fetch_and_write_txt_data(folder_name, filename, url):
    '''
    Fetchs text data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    '''
    Fetchs Excel data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url Excel
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    '''
    Fetchs CSV data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    '''
    Fetchs JSON data from a URL and writes it to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param url: URL to fetch the data from
    '''
    response = requests.get(url) # retrieves data from url text
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def write_txt_file(folder_name, filename, txt_data):
    '''
    writes text data to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param data: Text data to write to the file
    '''
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(txt_data)
        print(f"Text data saved to {file_path}")


def write_excel_file(folder_name, filename, excel_data):
    '''
    writes Excel data to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param data: Excel data to write to the file
    '''
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(excel_data)
        print(f"Excel data saved to {file_path}")

def write_csv_file(folder_name, filename, csv_data):
    '''
    writes CSV data to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param data: CSV data to write to the file
    '''
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(csv_data)
        print(f"Text data saved to {file_path}")

def write_json_file(folder_name, filename, json_data):
    '''
    writes JSON data to a file.
    :param folder_name: Name of the folder to save the data to
    :param filename: Name of the file to save the data to
    :param data: JSON data to write to the file
    '''
    file_path = Path(folder_name).join_path(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(json_data)
        print(f"Text data saved to {file_path}")




def main():
    '''
    Main function
    '''
    print(f"Name:  {utils.company_name}")
    
    url_text = "https://shakespeare.mit.edu/comedy_errors/full.html"
    url_excel = "insert excel url here"
    url_csv = "insert csv url here"
    url_json = "insert json url here"
    
    txt_folder_name = "data-txt"
    excel_folder_name = "data-excel"
    csv_folder_name = "data-csv"
    json_folder_name = "data-json"
    
    txt_filename = 'data.txt'
    excel_filename = 'data.xls'
    csv_filename = 'data.csv'
    json_filename = 'data.json'
    
    fetch_and_write_txt_data(txt_folder_name, txt_filename, url_text)
    #fetch_and_write_excel_data(excel_folder_name, excel_filename, url_excel)
    #fetch_and_write_csv_data(csv_folder_name, csv_filename, url_csv)
    #fetch_and_write_json_data(json_folder_name, json_filename, url_json)



# conditional execution
if __name__ == "__main__":
    main()