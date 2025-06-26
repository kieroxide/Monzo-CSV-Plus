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

    number_of_pies = 12
    months_to_plot = pivot_table.tail(number_of_pies) 
    cols = 3
    rows = int(number_of_pies / cols)
    fig, axs = plt.subplots(rows, cols, figsize=(cols*5, rows*5))
    axs = axs.flatten()

    for i, (month, data) in enumerate(months_to_plot.iterrows()):
        data = data[data > 5]  
        data = data.sort_values()
        axs[i].pie(
            data,
            startangle=90,
            counterclock=False,
            wedgeprops={'edgecolor': 'white', 'linewidth': 1}
        )
        axs[i].set_title(str(month))
        axs[i].axis('equal')  # keep pie circular

    plt.tight_layout()
    plt.legend(data.index
    )
    plt.show()

main()