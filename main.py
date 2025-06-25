import pandas as pd
import matplotlib.pyplot as plt

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    #formatting dataframe for graphable data
    df = read_clean_csv(filename)
    df_no_transfer = remove_category(df, category='Transfers')

    #Adds balance column
    df_no_transfer = calc_running_Balance(df_no_transfer)

    #Size of graph window in inches before DPI
    width = 16
    height = 8
    plt.figure(figsize=(width, height))
    
    plot_continuous_balance_graph(df_no_transfer)
    plot_continuous_balance_graph(df_no_transfer, 'Amount', 'red')
    plt.show()

def plot_continuous_balance_graph(df, y_axis='Balance', color = 'blue'):


    plt.plot(df['Date'], df[y_axis], linewidth=1, color=color)

    plt.title("Continuous Balance Over Time")
    plt.xlabel("Date")
    plt.ylabel(y_axis)
    #X-axis Line
    plt.axhline(0, color='black')
    plt.grid(True)
    plt.tight_layout()

def remove_category(df, category):
    #Removes rows with certain category
    filtered_df = df[df['Category'] != category].copy()
    return filtered_df

def calc_running_Balance(df):
    df = df.sort_values(by='Date')
    df['Balance'] = df['Amount'].cumsum()
    return df


def read_clean_csv(filename):
    df = pd.read_csv(filename)
    #Fills NaN with N/A for 'Name' column
    df['Name'] = df['Name'].fillna('N/A')

    #Drops NaN rows then drops NaN columns
    df.dropna(axis=1, inplace=True)  
    df.dropna(inplace=True)  

    #Converts Columns to correct type
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'])

    return df


main()