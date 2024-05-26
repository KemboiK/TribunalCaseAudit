import pandas as pd
import numpy as np
import warnings
warnings.filter = ("ignore")
import os

# Load the Excel file, skipping the first and second row and using the next two rows as headers
df = pd.read_excel('CASE AUDIT MAY.xlsx', sheet_name=1, header=[2, 3])

# The MultiIndex columns to inspect the hierarchical structure
print("MultiIndex columns:", df.columns)

# Drop rows that do not contain relevant data 
df.dropna(how='all', inplace=True)

# Flatten the MultiIndex to create single-level column names
df.columns = ['_'.join(filter(None, col)).strip() for col in df.columns.values]

# Rename the columns to remove 'Unnamed' and make them meaningful
df.columns = [col.replace('Unnamed: 0_level_0', '').replace('Unnamed: 1_level_0', '').replace('Unnamed: 2_level_0', '').strip() for col in df.columns]

# Print the cleaned columns
print("Cleaned columns:", df.columns)

# The first few rows of the DataFrame
print(df.head())

# Adjust the column name according to your actual data
outcome_column = 'What was the last outcome in Court_Outcome'  

# Filter rows where the Outcome column contains the word 'Active'
if outcome_column in df.columns:
    active_cases = df[df[outcome_column].str.contains('Active', case=False, na=False)]
    print(active_cases)
    #DataFrame to a CSV file
    active_cases.to_csv('active_cases.csv', index=False)

    # Extract inactive cases
    inactive_cases = df[~df[outcome_column].str.contains('Active', case=False, na=False)]
    print(inactive_cases)
    # Save inactive cases to CSV
    inactive_cases.to_csv('inactive_cases.csv', index=False)

else:
    print(f"Column'{outcome_column}' does not exist. Available columns are:",df.columns)

