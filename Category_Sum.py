import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    df = read_clean_csv(filename)

    #Formatting dataframe to series for plotting
    categories_to_filter = ['Transfers', 'Savings']
    filtered_df = remove_categories(df, categories_to_filter)
    df_spending = filtered_df[filtered_df['Amount'] < 0]
    category_sum = df_spending.groupby('Category')['Amount'].sum()
    category_sum = category_sum.abs()
    category_sum = category_sum.sort_values()
    
    
    plt.figure(figsize=(10, 10))
    category_sum.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False,
        cmap='Set3',  
        pctdistance=1.1,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
        labels=None
    )

    plt.legend(
        labels=category_sum.index,
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )
    
    plt.show()


main()