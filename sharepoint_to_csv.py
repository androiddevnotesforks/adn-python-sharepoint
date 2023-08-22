# sharepoint_to_csv.py

# Importing required libraries
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
from config import SHAREPOINT_SITE_URL, SHAREPOINT_LIST_NAME, SHAREPOINT_CLIENT_ID, SHAREPOINT_CLIENT_SECRET, CSV_FILE_PATH

# Creating client credentials
credentials = ClientCredential(SHAREPOINT_CLIENT_ID, SHAREPOINT_CLIENT_SECRET)

# Creating a client context
ctx = ClientContext(SHAREPOINT_SITE_URL).with_credentials(credentials)

# Accessing the SharePoint list
sp_list = ctx.web.lists.get_by_title(SHAREPOINT_LIST_NAME)

# Loading the list items
items = sp_list.get_items()
ctx.load(items)
ctx.execute_query()

# Creating an empty list to store the data
data = []

# Iterating over the SharePoint list
for item in items:
    # Appending the item properties to the list
    data.append(item.properties)

# Converting the list into a DataFrame
df = pd.DataFrame(data)

# Exporting the DataFrame to a CSV file
df.to_csv(CSV_FILE_PATH, index=False)
