from utils import *
import matplotlib.pyplot as plt

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    df = read_clean_csv(filename)
    df = remove_categories(df, ['Transfers', 'Savings', 'Bills'])
    spending_df = df[df['Amount'] < 0]

    #Monthly Column
    spending_df['YearMonth'] = spending_df['Date'].dt.to_period('M')

    monthly_category_sum = spending_df.groupby(['YearMonth', 'Category'])['Amount'].sum().abs()
    #Creates table of months and category
    pivot_table = monthly_category_sum.unstack(fill_value=0)
    pivot_table = pivot_table.div(pivot_table.sum(axis=1), axis=0) * 100
    for month, data in pivot_table.iterrows():
        plot_pie(month, data)
    plt.show()

def plot_pie(month, data):
    data = data[data > 2.5]  # remove zero categories for clarity
    plt.figure(figsize=(6,6))
    plt.pie(
        data,
        labels=data.index,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False,
        wedgeprops={'edgecolor': 'teal', 'linewidth': 1}
    )
    plt.title(f"Spending by Category for {month}")
main()