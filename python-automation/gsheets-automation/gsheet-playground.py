import gspread
from google.oauth2.service_account import Credentials

print("We will connect to google spreadsheet")

scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file('gsheets-sa-credentials.json', scopes=scope)
client = gspread.authorize(creds)

# Now we can open a gsheet

sheet = client.open('LabTracker').sheet1

print ("Connected to gsheet")

# We will print some value from Sheet

cellb6 = sheet.acell('B6').value
print (f"Value at cell B6 is {cellb6}")

print (f" Amina's github URL is {sheet.acell('D1').value}")


# We will try to extract just the username from github URL

a_url = sheet.acell('D1').value
print (f"Amina's Github URL is {a_url}")

print ("Extracting username from url")


# https://github.com/Amina558
url_split = a_url.split('/')



print (f"URL_split = {url_split}")
a_username = url_split[-1]
print (f" Aminas Github Username is : {a_username}")

# List all repos column

col_repo = sheet.col_values(3)[5:] # 3 = C5 onwards
print (f"Column C is {col_repo}")


# Write a cell in sheet

sheet.update_acell('B1', 'Some Text from python')