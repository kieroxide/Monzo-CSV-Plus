import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    df = read_clean_csv(filename)

    #Formatting dataframe to series for plotting
    category_percentages = format_for_pie(df)

    #Plots pie
    plt.figure(figsize=(10, 10))
    plot_pie(category_percentages)
    plt.show() #display pie

def format_for_pie(df):
    categories_to_filter = ['Transfers', 'Savings', 'Bills']
    filtered_df = remove_categories(df, categories_to_filter)

    df_spending = filtered_df[filtered_df['Amount'] < 0]

    #Sums, sorts and absolutes spending by category 
    category_sum = df_spending.groupby('Category')['Amount'].sum()
    category_sum = category_sum.abs()
    category_sum = category_sum.sort_values()

    total_spending = category_sum.sum()

    category_percentages = (category_sum / total_spending) * 100
    category_percentages = category_percentages[category_percentages > 2.5]
    return category_percentages

def plot_pie(df):
    df.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False,
        cmap='Set3',  
        pctdistance=1.15,
        wedgeprops={'edgecolor': 'grey', 'linewidth': 1},
        labels=None,
    )
    plt.title("Spending Proportions")
    plt.ylabel("")
    plt.legend(
        labels=df.index,
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

main()