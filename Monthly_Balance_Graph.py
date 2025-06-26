import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    DF = read_clean_csv(filename) #constant Dataframe
    df = DF.copy() #mutable copy

    prepare_and_plot_monthly_data(df)
    plt.show()

def prepare_and_plot_monthly_data(df):
    #Filter unneeded categories
    categories_to_filter = ['Transfers', 'Savings']
    df_filtered = remove_categories(df, categories_to_filter)

    #Create 3 new dataframes for each type of data
    spending = df_filtered[df_filtered['Amount'] < 0]
    income = df_filtered[df_filtered['Amount'] > 0]
    balance = calc_running_Balance(df_filtered)

    #Creates monthly series of each datatype and combines into one dataframe
    combined_monthly = group_monthly_combine(balance, spending, income)

    #Formats datetime column to just be year-month
    combined_monthly.index = combined_monthly.index.to_period('M')
    #Plots group Bar chart
    plot_multibar(combined_monthly)
    plt.show()
    
def plot_multibar(combined_monthly):
    combined_monthly.plot(
    kind='bar',
    figsize=(12, 6),
    width = 0.8
    )
    plt.axhline(color='black')
def group_monthly_combine(balance, spending, income):
    balance_monthly = balance.groupby(
    pd.Grouper(key='Date', freq='ME')
    )['Amount'].sum()

    spending_monthly = spending.groupby(
    pd.Grouper(key='Date', freq='ME')
    )['Amount'].sum()

    income_monthly = income.groupby(
    pd.Grouper(key='Date', freq='ME')
    )['Amount'].sum()

    combined_monthly = pd.DataFrame({
        'Balance' : balance_monthly,
        'Spending' : spending_monthly,
        'Income' : income_monthly
    })
    return combined_monthly

main()