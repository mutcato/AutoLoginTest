import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("/home/pi/Public/eksilogin/Sheet-8e4ca37a3adf.json", scope)

    gc = gspread.authorize(credentials)

    wks = gc.open(sheet_name).sheet1
    return wks

