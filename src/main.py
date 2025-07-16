from excel_reader import read_excel
from plot_generator import plot_delivery_status

# Name of the Excel file
file_name = "sample_orders.xlsx"

# Read and process the Excel file
df = read_excel(file_name)

# Show results and plot chart
if df is not None:
    print("\n✅ Orders and delivery status:")
    print(df[["Order ID", "Delivery Date", "Actual Delivery", "On Time", "Delay (days)"]])

    # Create and show the plot
    plot_delivery_status(df)
else:
    print("❌ Failed to load the Excel file.")
