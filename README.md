# Setup

## Create a Google Sheets file 
Format:

||A|B|C|
|-|-|-|-|
|1|MSFT|=GOOGLEFINANCE(A1)|=ifna(index(GOOGLEFINANCE(A1, "price", today()-1, 1),2,2),B1)|
|2|NIFTY|=GOOGLEFINANCE(A2)|=ifna(index(GOOGLEFINANCE(A2, "price", today()-1, 1),2,2),B2)|

## Create a config file

Copy the sheet ID. (Hint: "https://docs.google.com/spreadsheets/d/\<sheet-id\>/edit#gid=0")

Create a `config.json` in the project root.
```json
{
    "SpreadsheetId": "sheet-id"
}
```

## Enable the Google sheets API
GOTO https://developers.google.com/sheets/api/quickstart/python

Create a project with OAuth for Desktop enabled project and download `credentials.json` in the project root.

## Setup dependencies

```bash
pip install -r requirements.txt
```

## Install Tkinter

### Arch

```
pacman -S tk
```

### Debian

```
apt install python3-tk
```

# Usage

## CLI

```bash
# Authorize the application
python3 -m pygfbar.cli auth

# Fetch data from sheets
python3 -m pygfbar.cli fetch
>> SENSEX 38697.05 38697.05 0.00% NIFTY 11416.95 11416.95 0.00%

# Start the dock; left click to close
python3 -m pygfbar.cli dock --position 12
```