# sharepoint_to_csv.py

# Importing required libraries
from sharepoint import SharePointSite, basic_auth_opener
from config import SHAREPOINT_SITE_URL, SHAREPOINT_LIST_NAME, SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD, CSV_FILE_PATH
import pandas as pd

# Creating a new opener
opener = basic_auth_opener(SHAREPOINT_SITE_URL, SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD)

# Accessing the SharePoint site
site = SharePointSite(SHAREPOINT_SITE_URL, opener)

# Accessing the SharePoint list
sp_list = site.lists[SHAREPOINT_LIST_NAME]

# Creating an empty list to store the data
data = []

# Iterating over the SharePoint list
for row in sp_list.rows:
    # Appending the row data to the list
    data.append(row)

# Converting the list into a DataFrame
df = pd.DataFrame(data)

# Exporting the DataFrame to a CSV file
df.to_csv(CSV_FILE_PATH, index=False)
