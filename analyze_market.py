import pandas as pd

def analyze_market():
    # Read data from stock_data.csv
    try:
        stock_data = pd.read_csv('stock_data.csv')
    except FileNotFoundError:
        print("Error: 'stock_data.csv' not found.")
        return

    # Check if the file is empty
    if stock_data.empty:
        print("The stock data file is empty.")
        return

    # Analyze overall market trends
    overall_avg_price = stock_data['Price'].mean()
    overall_max_price = stock_data['Price'].max()
    overall_min_price = stock_data['Price'].min()
    overall_std_dev = stock_data['Price'].std()

    # Find stocks with the highest and lowest prices
    max_price_stock = stock_data.loc[stock_data['Price'].idxmax(), ['Stock', 'Date']]
    min_price_stock = stock_data.loc[stock_data['Price'].idxmin(), ['Stock', 'Date']]

    # Analyze trends for each stock
    stock_trends = stock_data.groupby('Stock').agg(
        Avg_Price=('Price', 'mean'),
        Max_Price=('Price', 'max'),
        Min_Price=('Price', 'min'),
        Std_Dev=('Price', 'std')
    ).reset_index()

    # Prepare the report
    report = (
        "Market Analysis Report\n"
        "=======================\n"
        f"Overall Average Price: {overall_avg_price:.2f}\n"
        f"Overall Maximum Price: {overall_max_price:.2f} (Stock: {max_price_stock['Stock']} on {max_price_stock['Date']})\n"
        f"Overall Minimum Price: {overall_min_price:.2f} (Stock: {min_price_stock['Stock']} on {min_price_stock['Date']})\n"
        f"Overall Price Standard Deviation: {overall_std_dev:.2f}\n\n"
        "Stock-Specific Analysis:\n"
        "-------------------------\n"
    )

    for _, row in stock_trends.iterrows():
        report += (
            f"Stock: {row['Stock']}\n"
            f"  Average Price: {row['Avg_Price']:.2f}\n"
            f"  Maximum Price: {row['Max_Price']:.2f}\n"
            f"  Minimum Price: {row['Min_Price']:.2f}\n"
            f"  Price Standard Deviation: {row['Std_Dev']:.2f}\n\n"
        )

    # Save the report to a file
    # with open('market_analysis.txt', 'w') as report_file:
    #     report_file.write(report)

    # print("Market analysis report has been written to 'market_analysis.txt'.")

if __name__ == "__main__":
    analyze_market()