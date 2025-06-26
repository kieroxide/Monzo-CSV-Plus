import pandas as pd

def read_clean_csv(filename):
    """
    Read and clean a CSV file containing financial transaction data.
    
    Args:
        filename (str): Path to the CSV file to read
        
    Returns:
        pandas.DataFrame: Cleaned DataFrame with proper data types and no NaN values
        
    Notes:
        - Fills NaN values in 'Name' column with 'N/A'
        - Drops columns and rows containing NaN values
        - Converts 'Date' column to datetime with day-first format
        - Converts 'Time' column to datetime format
    """
    df = pd.read_csv(filename)
    #Fills NaN with N/A for 'Name' column
    df['Name'] = df['Name'].fillna('N/A')

    #Drops NaN rows then drops NaN columns
    df.dropna(axis=1, inplace=True)  
    df.dropna(inplace=True)  

    #Converts Columns to correct type
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

    return df

def calc_running_Balance(df):
    """
    Calculate running balance for financial transactions.
    
    Args:
        df (pandas.DataFrame): DataFrame containing transaction data with 'Date' and 'Amount' columns
        
    Returns:
        pandas.DataFrame: DataFrame with added 'Balance' column showing cumulative running balance
        
    Notes:
        - Sorts DataFrame by date before calculating balance
        - Calculates cumulative sum of 'Amount' column
        - Rounds balance to 2 decimal places
    """
    df = df.sort_values(by='Date')
    df['Balance'] = df['Amount'].cumsum()
    df['Balance'] = round(df['Balance'], 2)
    return df

def remove_categories(df, categories):
    """
    Remove transactions of a specific category from the DataFrame.
    
    Args:
        df (pandas.DataFrame): DataFrame containing transaction data with 'Category' column
        categories (Array[str]): Categories name to filter out from the data
        
    Returns:
        pandas.DataFrame: New DataFrame with specified category removed
        
    Notes:
        - Creates a copy of the filtered DataFrame to avoid modifying original data
        - Removes all rows where 'Category' column matches the specified categories
    """
    #Removes rows with certain categor
    filtered_df = df.copy()
    for category in categories:
        filtered_df = filtered_df[filtered_df['Category'] != category]
    return filtered_df
