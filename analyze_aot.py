import pandas as pd

def analyze_aot_stock():
    # Read stock data from CSV
    try:
        stock_data = pd.read_csv('stock_data.csv')
    except FileNotFoundError:
        print("Error: 'stock_data.csv' not found.")
        return

    # Filter data for AOT stock
    aot_data = stock_data[stock_data['Stock'] == 'AOT']

    if aot_data.empty:
        print("No data found for AOT stock.")
        return

    # Perform analysis
    avg_price = aot_data['Price'].mean()
    max_price = aot_data['Price'].max()
    min_price = aot_data['Price'].min()
    std_dev_price = aot_data['Price'].std()
    median_price = aot_data['Price'].median()
    total_volume = aot_data['Volume'].sum() if 'Volume' in aot_data.columns else "N/A"

    # Prepare analysis report
    report = (
        "AOT Stock Analysis Report\n"
        "==========================\n"
        f"Average Price: {avg_price:.2f}\n"
        f"Maximum Price: {max_price:.2f}\n"
        f"Minimum Price: {min_price:.2f}\n"
        f"Standard Deviation of Price: {std_dev_price:.2f}\n"
        f"Median Price: {median_price:.2f}\n"
        f"Total Trading Volume: {total_volume}\n"
    )

    # Write report to file
    with open('aot_analysis.txt', 'w') as report_file:
        report_file.write(report)

    print("AOT stock analysis report has been written to 'aot_analysis.txt'.")

if __name__ == "__main__":
    analyze_aot_stock()