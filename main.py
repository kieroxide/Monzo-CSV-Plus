import pandas as pd
import matplotlib.pyplot as plt

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    DF = read_clean_csv(filename) #constant Dataframe
    df = DF.copy() #mutable copy

    prepare_and_plot_daily_balance(df)
    plt.show()

def prepare_and_plot_daily_balance(df):
    df = remove_category(df, category='Transfers')
    df = remove_category(df, category='Savings')

    #Sums all transactions by date, calculates balance
    df = df.groupby('Date')['Amount'].sum().reset_index()
    df = calc_running_Balance(df)

    #displays graph
    plot_continuous_graph(df, y_axes=['Balance', 'Amount'], colors=['blue', 'green'])

def plot_continuous_graph(df, y_axes = [], colors = [], width = 12, height = 8):
    #Size of graph window in inches before DPI
    plt.figure(figsize=(width, height))
    for axis, color in zip(y_axes,colors):
        plot_line(df, y_axis=axis, color=color)
    
    plt.title("Continuous Balance Over Time")
    plt.axhline(0, color='black') #X-axis Line
    plt.xlabel("Date")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()

def plot_line(df, y_axis='Balance', color = 'blue'):
    plt.plot(df['Date'], df[y_axis], linewidth=1, color=color, label=y_axis)

def remove_category(df, category):
    #Removes rows with certain category
    filtered_df = df[df['Category'] != category].copy()
    return filtered_df

def calc_running_Balance(df):
    df = df.sort_values(by='Date')
    df['Balance'] = df['Amount'].cumsum()
    df['Balance'] = round(df['Balance'], 2)
    return df


def read_clean_csv(filename):
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


main()