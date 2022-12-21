
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from prettytable import PrettyTable
import csv
import datetime
import json
import os
import click
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the spreadsheet ID and range for the data page
SPREADSHEET_ID = '1ndlIyYhAmGTBoZtT3sPEgpV5b_Bug4vPjHSGHxnAk9Y'
DATA_RANGE_NAME = 'data!A1:M'

# Set the column names for the datetime start and end columns
DATETIME_START_COLUMN = 'datetime_start'
DATETIME_END_COLUMN = 'datetime_end'
REPORTED_AT_COLUMN = 'reported_at'

# Set the date format for the datetime columns
DATE_FORMAT = '%d.%m.%Y %H:%M:%S'

def download_data(experiment_id, file_format, path):
    """
    Downloads data from Google Sheets and exports the rows from the given experiment.

    Parameters:
        experiment_id (int): Id of the experiment to download.
        file_format (str): Format of the file to export.
    """
    # Authenticate and create a service object
    service = get_service()

    # Get the data from metadata and data page
    data = get_data(service, SPREADSHEET_ID, "data")
    metadata = get_data(service, SPREADSHEET_ID, "metadata")

    assert len(metadata) > experiment_id, f"Experiment with id {experiment_id} not found!"

    # get datetime column indices
    datetime_start_index = metadata[0].index(DATETIME_START_COLUMN)
    datetime_end_index = metadata[0].index(DATETIME_END_COLUMN)

    # get start and end dates of last experiment
    start_date = metadata[experiment_id][datetime_start_index]
    end_date = metadata[experiment_id][datetime_end_index]

    # Convert the start and end dates to datetime objects
    start_date = datetime.datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.datetime.strptime(end_date, DATE_FORMAT)

    # Get the reported_at column index
    reported_at_index = data[0].index(REPORTED_AT_COLUMN)

    # Filter the data based on the start and end dates
    filtered_data = [
        row 
        for row in data[1:] 
        if start_date <= datetime.datetime.strptime(row[reported_at_index], DATE_FORMAT) <= end_date
    ]

    assert len(filtered_data) > 0, f"No Data found for experiment with id {experiment_id}. Please check if the date range is correct!"

    # Normalize Data
    normalized_data = normalize_data(filtered_data, data[0])

    experiment_name = f"Experiment_{experiment_id}"

    # Write the filtered data to a CSV file
    write_data(normalized_data[1:], normalized_data[0], path, experiment_name, file_format)

def normalize_data(data, columns):
    """
    Normalizes the data by extracting the JSON objects from the 'hotspot' column and adding them as new rows.

    Parameters:
        data (list): A list of rows where each row is a list of values.
        columns (list): A list of column names for the data.

    Returns:
        list: A list of rows with the JSON objects extracted and added as new rows.
    """
    # Extract the keys from the first JSON object
    json_array = json.loads(data[0][3])
    keys = list(json_array[0].keys())

    # Add the keys to the list of column names
    columns = columns[:3] + [f"hotspot_{key}" for key in keys] + columns[4:-1]

    normalized_data = [columns]
    for row in data:
        # Parse the JSON string and extract the array of objects
        json_array = json.loads(row[3])
        for json_obj in json_array:
            # Create a new row for each object in the array
            new_row = row[:3] + [json_obj[key] if key in json_obj else "" for key in keys] + row[4:]

            # convert node_lat and node_long
            new_row[1] = float(new_row[1].replace(",","."))
            new_row[2] = float(new_row[2].replace(",","."))

            normalized_data.append(new_row)
    return normalized_data

def get_service():
    """
    Authenticates and returns a service object for interacting with Google Sheets.
    """

    api_key = os.getenv('API_KEY')

    # If an API key is specified in the .env file, use it to authenticate
    assert api_key, "Environment variable 'API_KEY' not found in current env. Please specify!"
    
    # Create a service object
    service = build('sheets', 'v4', developerKey=api_key)

    return service

def get_data(service, spreadsheet_id, page_name):
    """
    Gets the data from a Google Sheets page.

    Args:
        service: The Google Sheets service object
        spreadsheet_id: The ID of the spreadsheet
        page_name: Name of the page in the Google Sheet

    Returns:
        A list of lists representing the rows and cells of the data
    """

    # Call the Sheets API to get the sheet with the given name
    sheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute().get('sheets', [])
    sheet = None
    for s in sheets:
        if s.get('properties', {}).get('title', '') == page_name:
            sheet = s
            break

    if not sheet:
        print(f'Sheet with name "{page_name}" not found')
        return []

    # Get the number of rows and columns in the sheet
    num_rows = sheet.get('properties', {}).get('gridProperties', {}).get('rowCount', 0)
    num_cols = sheet.get('properties', {}).get('gridProperties', {}).get('columnCount', 0)

    # Call the Sheets API to get the values in the sheet
    range_name = f'{page_name}!A1:{chr(ord("A") + num_cols - 1)}{num_rows}'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    return values

def write_data(data, column_names, path, output_filename, file_format="csv"):
    """
    Writes the data to a file in the specified format.

    Args:
        data: A list of lists representing the rows and cells of the data
        column_names: A list of strings representing the column names
        output_filename: The name of the output file
        file_format: The format of the output file (csv, pickle, excel, parquet) (default: csv)
    """
    if file_format == 'csv':
        df = pd.DataFrame(data, columns=column_names)
        df.to_csv(os.path.join(path, output_filename) + ".csv", index=False)

    elif file_format == 'pickle':
        with open(os.path.join(path, output_filename)  + ".pkl", 'wb') as picklefile:
            pickle.dump(data, picklefile)
    elif file_format == 'excel':
        df = pd.DataFrame(data, columns=column_names)
        df.to_excel(os.path.join(path, output_filename + ".xlsx"), index=False)
    elif file_format == 'parquet':
        df = pd.DataFrame(data, columns=column_names)
        df.to_parquet(os.path.join(path, output_filename + ".parquet"), index=False)
    else:
        raise ValueError(f"Invalid file format: {file_format}")

def print_experiment_table(data):
    """
    Prints the experiment table to the console.

    Parameters:
        data (list): A list of rows where each row is a list of values. The first row should contain the column names.
    """
    # Create a table
    table = PrettyTable()

    # Set the column names
    table.field_names = data[0]

    # Add the rows to the table
    for row in data[1:]:
        table.add_row(row)

    # Print the table
    print(table)
    print()

@click.command()
@click.option('--id', type=int, help='The index of the row in the metadata page to use for filtering.')
@click.option('--last', is_flag=True, help='Downloads the latest experiment data.')
@click.option("--file_format", default="csv", type=str, help="Defines the format for the output file. (csv, pickle, excel, parquet)")
@click.option("--path", default="./data/raw/", type=str, help="Defines the path to export the file to.")
def main(id, last, file_format, path):
    if id is not None:
        download_data(id, file_format, path)
    else:
        # Get the metadata page data
        service = get_service()
        metadata = get_data(service, SPREADSHEET_ID, "metadata")

        if last:
            last_id = int(metadata[-1][0])
            print(f"Downloading latest experiment with id {last_id}")
            download_data(last_id, file_format, path)


        print_experiment_table(metadata)
        id = click.prompt('Enter the ID of the experiment you want to extract', type=int)
        download_data(id, file_format, path)
    print("done!")

main()