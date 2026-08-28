import os
import gspread
import requests
from google.oauth2.service_account import Credentials
from gspread.utils import rowcol_to_a1 # Helper to convert coordinates like (6, 4) into "D6"

# ==========================================
# 1. SETUP SECRETS, COLORS & CONNECTION
# ==========================================

# Grab the GitHub Personal Access Token (PAT) from your computer's memory.
# This acts as our VIP pass so GitHub doesn't block us for checking too many students.
GITHUB_TOKEN = os.getenv("LAB_TRK_PAT")

# DEBUG: Check if the token was found (Uncomment the line below to test)
# print(f"DEBUG: Token loaded successfully? {'Yes' if GITHUB_TOKEN else 'No'}")

# Define our colors using Google's RGB format (0.0 is zero color, 1.0 is max color)
green_format = {
    "backgroundColor": {"red": 0.85, "green": 0.93, "blue": 0.82}, # Light green background
    "textFormat": {"foregroundColor": {"red": 0.0, "green": 0.5, "blue": 0.0}} # Dark green text
}
red_format = {
    "backgroundColor": {"red": 0.96, "green": 0.8, "blue": 0.8}, # Light red background
    "textFormat": {"foregroundColor": {"red": 0.7, "green": 0.0, "blue": 0.0}} # Dark red text
}

print("Connecting to Google Sheets...")
# Tell Google what we want permission to do (read/edit spreadsheets)
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
# Load the password file (credentials.json)
creds = Credentials.from_service_account_file('gsheets-sa-credentials.json', scopes=scopes)
# Log in!
client = gspread.authorize(creds)
# Open the specific file and tab
sheet = client.open('LabTracker').sheet1

# ==========================================
# 2. GITHUB CHECKER FUNCTION
# ==========================================
def check_github(github_url, repo_name, lab_number):
    """Takes a student's URL, finds their username, and checks their GitHub repo."""
    
    # Safety Check: If the spreadsheet has a blank cell or "NaN" for the URL, skip it.
    if not github_url or github_url.lower() == "nan":
        return False
        
    # Extract the username: Take the URL, chop it into pieces by the '/' symbol, 
    # and grab the very last piece (which is the username).
    username = github_url.rstrip('/').split('/')[-1]
    
    # DEBUG: See what username we extracted (Uncomment to test)
    # print(f"DEBUG: Extracted username '{username}' from URL '{github_url}'")
    
    # This is the exact link GitHub uses to show the files inside a repository
    api_link = f"https://api.github.com/repos/{username}/{repo_name}/contents/"
    
    # DEBUG: See the exact API link we are about to visit (Uncomment to test)
    # print(f"DEBUG: Visiting GitHub API -> {api_link}")
    
    # Prepare to show GitHub our VIP pass (the token)
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
        
    # Send the request to GitHub to get the files
    response = requests.get(api_link, headers=headers)
    
    # DEBUG: See what GitHub said back. 200 means OK, 404 means Not Found.
    # print(f"DEBUG: GitHub responded with status code: {response.status_code}")
    
    # If the page doesn't exist or is private, return False (Lab not done)
    if response.status_code != 200:
        return False 
        
    # Convert GitHub's answer into a Python list, and check every single file
    for file in response.json():
        # If the file name starts with our lab number (e.g., "1-script.py" starts with "1")
        if file['name'].startswith(str(lab_number)):
            return True # We found it! They did the homework.
            
    # If the loop finishes checking every file and finds nothing, return False
    return False

# ==========================================
# 3. READ DATA & PREPARE BULK UPDATES
# ==========================================
print("Downloading sheet data... (This counts as 1 API Request to Google)")
# Download the entire spreadsheet into Python's memory instantly
all_data = sheet.get_all_values()

# Grab the list of student GitHub URLs.
# In Python, all_data[0] is the very first row. [3:] means "skip the first 3 columns, grab the rest".
student_urls = all_data[0][3:]

# DEBUG: Print the exact list of URLs we grabbed from Row 1 (Uncomment to test)
# print(f"DEBUG: Found these student URLs: {student_urls}")

# These lists will act as our "shopping carts". We will put all our planned changes
# in here, and send them to Google all at once at the very end.
text_updates = []
color_updates = []

print("Checking GitHub for all students and labs. This might take a moment...")

# Loop through the rows, starting at Row 6 in the spreadsheet (which is index 5 in Python).
for row_index in range(5, len(all_data)):
    row = all_data[row_index]
    
    # Get the lab number and repo name for this specific row, and clean up any accidental spaces (.strip)
    lab_number = row[0].strip() # Column A
    repo_name = row[2].strip()  # Column C
    
    # If there is no lab number on this row, skip it and move to the next row
    if not lab_number or not repo_name:
        continue
    
    # DEBUG: See which lab we are currently checking (Uncomment to test)
    print(f"\nDEBUG: --- Now checking Lab {lab_number} in repo '{repo_name}' ---")
        
    # Now, loop through every single student URL we found earlier
    for col_offset in range(len(student_urls)):
        url = student_urls[col_offset]
        
        # Calculate exactly where we are on the grid so we know where to color
        excel_row = row_index + 1      # Spreadsheets start at row 1, Python starts at 0
        excel_col = col_offset + 4     # Students start at Column D (which is column number 4)
        
        # Run our GitHub check!
        did_homework = check_github(url, repo_name, lab_number)
        
        # Decide what to write and what color to use based on the answer
        if did_homework == True:
            cell_text = "Yes"
            cell_color = green_format
        else:
            cell_text = "No"
            cell_color = red_format
            
        # DEBUG: See the final result before it goes into the shopping cart
        # print(f"DEBUG: Row {excel_row}, Col {excel_col} -> Writing '{cell_text}'")
            
        # 1. Put the Text Update in our shopping cart
        text_updates.append(gspread.Cell(excel_row, excel_col, cell_text))
        
        # 2. Put the Color Update in our shopping cart
        # (Google needs cell names like "D6" for colors, so we convert the numbers to letters)
        cell_name = rowcol_to_a1(excel_row, excel_col)
        color_updates.append({
            "range": cell_name,
            "format": cell_color
        })

# DEBUG: See how many items are in our shopping carts before checkout (Uncomment to test)
# print(f"\nDEBUG: Prepared {len(text_updates)} text changes and {len(color_updates)} color changes.")

# ==========================================
# 4. PUSH ALL UPDATES AT ONCE
# ==========================================
print("Pushing all updates to Google Sheets... (This counts as 2 API Requests)")

# "Checkout!" - Send the text cart to Google
if text_updates:
    sheet.update_cells(text_updates)

# "Checkout!" - Send the color cart to Google
if color_updates:
    sheet.batch_format(color_updates)

print("✅ Bulk update complete!")