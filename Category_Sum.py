import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    df = read_clean_csv(filename)

    #Formatting dataframe to series for plotting
    categories_to_filter = ['Transfers', 'Savings', 'Bills']
    filtered_df = remove_categories(df, categories_to_filter)
    df_spending = filtered_df[filtered_df['Amount'] < 0]
    category_sum = df_spending.groupby('Category')['Amount'].sum()
    category_sum = category_sum.abs()
    category_sum = category_sum.sort_values()
    total_spending = category_sum.sum()
    category_percentages = (category_sum / total_spending) * 100
    category_percentages = category_percentages[category_percentages > 2.5]
    print(category_percentages)

    plt.figure(figsize=(10, 10))
    category_percentages.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False,
        cmap='Set3',  
        pctdistance=1.15,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
        labels=None,
    )
    plt.ylabel("")
    plt.legend(
        labels=category_percentages.index,
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    plt.show()


main()