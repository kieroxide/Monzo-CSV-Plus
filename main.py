import pandas as pd
import matplotlib.pyplot as plt

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    #formatting dataframe for graphable data
    df = read_clean_csv(filename)
    df_no_transfer = remove_category(df, category='Transfers')
    df_no_savings = remove_category(df_no_transfer, category='Savings')
    print(df_no_savings.to_string())
    #Adds balance, income, spending column, DAILY
    df_sum = df_no_savings.groupby('Date')['Amount'].sum().reset_index()
    df_formatted = calc_running_Balance(df_sum)
    ### NEED TO FIGURE OUT GOOD NAMING FOR ALL THESE DATAFRAMES
    df_formatted['Income'] = df_formatted['Amount'].where(df_formatted['Amount'] > 0)
    df_formatted['Spending'] = df_formatted['Amount'].where(df_formatted['Amount'] < 0)
    print(df_formatted.to_string())
    plot_continuous_graph(df_formatted, y_axes=['Balance', 'Amount'], colors=['blue', 'green'])
    plt.show()

def plot_continuous_graph(df, y_axes = [], colors = [], width = 12, height = 8):
    #Size of graph window in inches before DPI
    plt.figure(figsize=(width, height))
    for axis, color in zip(y_axes,colors):
        plot_line(df, y_axis=axis, color=color)

    plt.legend()

def plot_line(df, y_axis='Balance', color = 'blue'):
    plt.plot(df['Date'], df[y_axis], linewidth=1, color=color, label=y_axis)
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