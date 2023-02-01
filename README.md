# Broker Trade Summary

## Introduction
A script that get data of  broker trade summary of NEPSE and creates a CSV file.The script to run at 4 PM NST 

## Requirements
- `requests` library
- `csv` library

## Usage
1. Clone this repository to your local machine
2. Install the required libraries by running `pip install -r requirements.txt`
3. Run the script `python main.py`

## Script Explanation
The script retrieves data from the website and converts it to a JSON object. The data is then processed and sorted by `total_purch_amount`. The processed data is then written to a CSV file with the file name being the date of data collection.

The columns in the CSV file are:
- `broker_number`
- `total_purch_amount`
- `total_purch(%)`
- `total_sell_amount`
- `total_sell(%)`
- `matching_summary`
- `matching(%)`
- `total_turn_over(%)`
- `turn_over_vs_market`
- `Buy/Sell_Ratio`
