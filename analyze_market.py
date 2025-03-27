import pandas as pd

def analyze_market():
    # อ่านข้อมูลจากไฟล์ stock_data.csv
    try:
        stock_data = pd.read_csv('stock_data.csv')
    except FileNotFoundError:
        print("Error: 'stock_data.csv' not found.")
        return

    # ตรวจสอบว่ามีข้อมูลในไฟล์หรือไม่
    if stock_data.empty:
        print("The stock data file is empty.")
        return

    # วิเคราะห์แนวโน้มราคาหุ้นโดยรวม
    overall_avg_price = stock_data['Price'].mean()
    overall_max_price = stock_data['Price'].max()
    overall_min_price = stock_data['Price'].min()
    overall_std_dev = stock_data['Price'].std()

    # คำนวณหุ้นที่มีราคาสูงสุดและต่ำสุด
    max_price_stock = stock_data.loc[stock_data['Price'].idxmax(), 'Stock']
    min_price_stock = stock_data.loc[stock_data['Price'].idxmin(), 'Stock']

    # เตรียมรายงานผลการวิเคราะห์
    report = (
        "Market Analysis Report\n"
        "=======================\n"
        f"Overall Average Price: {overall_avg_price:.2f}\n"
        f"Overall Maximum Price: {overall_max_price:.2f} (Stock: {max_price_stock})\n"
        f"Overall Minimum Price: {overall_min_price:.2f} (Stock: {min_price_stock})\n"
        f"Overall Price Standard Deviation: {overall_std_dev:.2f}\n"
    )

    # บันทึกผลการวิเคราะห์ลงในไฟล์ market_analysis.txt
    with open('market_analysis.txt', 'w') as report_file:
        report_file.write(report)

    print("Market analysis report has been written to 'market_analysis.txt'.")

if __name__ == "__main__":
    analyze_market()