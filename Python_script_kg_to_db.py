import pandas as pd
import kaggle as kg
import os
import json
from sqlalchemy import create_engine, MetaData

def download_kaggle_dataset(dataset, download_path):
    """
    Download a dataset from Kaggle and unzip it into a specified folder.

    Parameters:
        dataset (str): The dataset identifier from Kaggle (e.g., 'username/dataset-name').
        download_path (str): The local path where the dataset will be downloaded and unzipped.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Authenticate using the Kaggle API
    kg.api.authenticate()

    # Download and unzip the dataset
    kg.api.dataset_download_files(dataset, path=download_path, unzip=True)

def get_database_url(config_path='config.json'):
    """
    Reads database configuration from a JSON file and constructs a PostgreSQL connection URL.

    Args:
        config_path (str): The path to the JSON configuration file. Default is 'config.json'.

    Returns:
        str: A PostgreSQL connection URL constructed from the configuration details.
    """
    with open(config_path) as config_file:
        config = json.load(config_file)
    
    username = config['username']
    password = config['password']
    host = config['host']
    database = config['database']
    port_number = config['port_number']
    DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port_number}/{database}"
    
    return DATABASE_URL

def load_csv_db(csv_files, folder_path, engine):
    """
    Load CSV files into a SQL database.

    Parameters:
        csv_files (list of str): List of CSV file names (without the .csv extension) to be loaded into the database.
        folder_path (str): The directory where the CSV files are stored.
        engine: SQLAlchemy engine object for database connection.

    This function reads CSV files from the specified folder and loads each file into a table in the SQL database. 
    The table name corresponds to the CSV file name. If a table with the same name already exists, it will be replaced.

    Raises:
        Exception: If an error occurs during the loading process, it will be printed to the console.
    """
    for file_name in csv_files:
        file_path = os.path.join(folder_path, file_name + '.csv')
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
        try:
            df.to_sql(file_name, con=engine, if_exists='replace', index=False)
            print(f"{file_name} table created successfully.")
        except Exception as e:
            print(f"An error occurred while creating the table {file_name}: {e}")

# Dataset to download
dataset = 'prajwal6362venom/diwali-sales'

# Creating a new folder named "kaggle_dataset" in the current directory to store the dataset
download_path = './kaggle_diwali_sales/'

# Download Kaggle dataset
download_kaggle_dataset(dataset, download_path)

# Create database URL using config file containing database credentials
DATABASE_URL = get_database_url(config_path='config.json')
engine = create_engine(DATABASE_URL)

# Extract file names
csv_files = os.listdir(download_path)
csv_file_names = [file.replace('.csv', '') for file in csv_files if file.endswith('.csv')]

# Load CSV file/files into DB
load_csv_db(csv_file_names, download_path, engine)