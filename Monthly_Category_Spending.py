from utils import *
import matplotlib.pyplot as plt

def main():
    filename = "C:/Users/bailk/Desktop/Monzo Data Export - CSV (Friday, June 20th, 2025).csv"   
    df = read_clean_csv(filename)
    df = remove_categories(df, ['Transfers', 'Savings'])
    spending_df = df[df['Amount'] < 0]
    #Monthly Column
    spending_df['YearMonth'] = spending_df['Date'].dt.to_period('M')

    monthly_category_sum = spending_df.groupby(['YearMonth', 'Category'])['Amount'].sum().abs()
    pivot_table = monthly_category_sum.unstack(fill_value=0)
    
    pivot_table.plot(
        kind='bar',      # grouped bar chart (stacked=False is default)
        figsize=(12, 6),
        cmap='tab20'     # nice colors for categories
    )
    plt.title("Monthly Spending by Category")
    plt.ylabel("Amount")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
   
main()