# Overview
This script processes an Excel file (CASE AUDIT MAY.xlsx) containing case audit data, cleans the data, and filters it to identify active and inactive cases based on a specified column. The results are saved into separate CSV files.

# Prerequisites
Python 3.x
pandas
numpy
openpyxl (for reading Excel files)
# Setup
1.Ensure you have Python 3.x installed on your system.
2.Install the required libraries using pip:
pip install pandas numpy openpyxl
# Usage
1.Place the Excel file (CASE AUDIT MAY.xlsx) in the same directory as the script.
2.Run the script:
python script_name.py
# Script Description
1.Load Excel File: Skips the first two rows and uses the next two rows as headers.
2.Clean Data:
Drops rows that do not contain relevant data.
Flattens MultiIndex columns to create single-level column names.
Renames columns to remove 'Unnamed' and makes them meaningful.
3.Filter Cases:
Identifies and saves active cases (rows where the outcome column contains 'Active') to active_cases.csv.
Identifies and saves inactive cases (rows where the outcome column does not contain 'Active') to inactive_cases.csv.
## Key Variables
outcome_column: The name of the column used to determine the outcome of cases. Adjust this variable according to your actual data.
## Output
active_cases.csv: Contains rows where the outcome column indicates active cases.
inactive_cases.csv: Contains rows where the outcome column indicates inactive cases.
## Example Output
Active Cases: Displayed and saved to active_cases.csv.
Inactive Cases: Displayed and saved to inactive_cases.csv.
## Error Handling
If the outcome_column does not exist, the script will print an error message and list the available columns.
