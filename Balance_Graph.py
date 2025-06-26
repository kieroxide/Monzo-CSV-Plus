import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    DF = read_clean_csv(filename) #constant Dataframe
    df = DF.copy() #mutable copy

    prepare_and_plot_daily_balance(df)
    plt.show()

def prepare_and_plot_daily_balance(df):
    categories_to_filter = ['Transfers', 'Savings']
    df_filtered = remove_categories(df, categories_to_filter)

    #Sums all transactions by date, calculates balance
    df_daily_sum = df_filtered.groupby('Date')['Amount'].sum().reset_index()
    df_plot = calc_running_Balance(df_daily_sum)

    #displays graph
    plot_continuous_graph(df_plot, y_axes=['Balance', 'Amount'], colors=['blue', 'green'])

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

main()