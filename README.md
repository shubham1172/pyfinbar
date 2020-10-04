# Setup

## Create a Google Sheets file 
Format:

||A|B|C|
|-|-|-|-|
|1|MSFT|=GOOGLEFINANCE(A1)|=GOOGLEFINANCE(A1, "CloseYest")|
|2|NIFTY|=GOOGLEFINANCE(A2)|=GOOGLEFINANCE(A1, "CloseYest")|

## Create a config file

Copy the sheet ID. (Hint: "https://docs.google.com/spreadsheets/d/(sheet-id)/edit#gid=0")

Create a `config.json` in the project root.
```json
{
    "SpreadsheetId": "sheet-id",
    "MaxVisibleStocks": 8
}
```

_MaxVisibleStocks_ is number of stocks visible in the bar.

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