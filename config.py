# config.py

# Importing required libraries
from dotenv import load_dotenv
import os

# Loading the .env file
load_dotenv()

# SharePoint site URL
SHAREPOINT_SITE_URL = os.getenv('SHAREPOINT_SITE_URL')

# SharePoint list name
SHAREPOINT_LIST_NAME = os.getenv('SHAREPOINT_LIST_NAME')

# SharePoint username
SHAREPOINT_USERNAME = os.getenv('SHAREPOINT_USERNAME')

# SharePoint password
SHAREPOINT_PASSWORD = os.getenv('SHAREPOINT_PASSWORD')

# CSV file path
CSV_FILE_PATH = os.getenv('CSV_FILE_PATH')
