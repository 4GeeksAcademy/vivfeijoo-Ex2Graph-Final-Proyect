from excel_reader import read_excel
from plot_generator import plot_delivery_status, plot_delivery_delay
from ppt_creator import save_plot_to_ppt

file_name = "sample_orders.xlsx"
df = read_excel(file_name)

if df is not None:
    print("\n✅ Orders and delivery status:")
    print(df[["Order ID", "Delivery Date", "Actual Delivery", "On Time", "Delay (days)"]])

    # Show basic chart
    plot_delivery_status(df)

    # Save delay chart as image
    chart_path = "output/delay_chart.png"
    plot_delivery_delay(df, save=True, filename=chart_path)

    # Insert the image into PowerPoint
    ppt_path = "output/delivery_report.pptx"
    save_plot_to_ppt(chart_path, ppt_path)
else:
    print("❌ Failed to load the Excel file.")
