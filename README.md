# Pyfinbar

## Installation

- Go to https://github.com/shubham1172/pyfinbar/actions and select the latest workflow which ran successfully (one with a green tick next to it)
- Go to build-linux or build-windows depending on your Operating System
- Download artifact and extract it to a directory
- Edit the `stocks.json` file with appropriate values (see [Create a stocks file](./README.md#create-a-stocks-file)).
- Run pyfinbar

## Usage


```bash
# Fetch data from sheets
python3 -m pyfinbar.cli fetch
>> SENSEX 38697.05 38697.05 0.00% NIFTY 11416.95 11416.95 0.00%

# Start the dock; left click to close
python3 -m pyfinbar.cli dock --position 12 --refresh-rate 10
```

## Running from source

### Create a stocks file

Create a `stocks.json` in the project root.
```json
[
    {
        "Ticker": "NIFTY",
        "Symbol": "NSX",
        "Type": "INDEX"
    },
    {
        "Ticker": "YESBANK",
        "Symbol": "YB"
    }
]
```

For each stock,
- "Ticker" is the display name for PyFinBar
- "Symbol" is the moneycontrol symbol*
- "Type" can be "INDEX", "BSE", or "NSE" (default)


***Note**, goto moneycontrol.com and open the "network" tab under developer console. Lookout for API calls to https://priceapi.moneycontrol.com/ and get the symbol from there.

### Setup dependencies

```bash
pip install -r requirements.txt
```

### Install Tkinter

#### Arch

```
pacman -S tk
```

#### Debian

```
apt install python3-tk
```