import pandas as pd
import matplotlib.pyplot as plt
from utils import *

def main():
    #Need to sum all categories
    # and filter to just spending categories
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    df = read_clean_csv(filename)

    #filters to only spending
    df_spending = df[df['Amount'] < 0]
    category_sum = df_spending.groupby('Category')['Amount'].sum()
    print(category_sum)


main()