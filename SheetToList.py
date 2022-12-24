import pandas as pd


def sheetToList(location):
    # Variables to Change
    COLUMNNAME = "UPC"

    sheet = pd.read_excel(location)
    # sheet = pd.read_excel(location, sheet_name = "NAME") if multiple sheets exist.

    barcodeList = sheet[COLUMNNAME].tolist()
    
    return barcodeList