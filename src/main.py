from excel_reader import read_excel
from plot_generator import plot_delivery_status  # si lo tienes creado

# This is the name of your Excel file inside /data/
file_name = "sample_orders.xlsx"

# Call the function and get the data
df = read_excel(file_name)

if df is not None:
    print("\n✅ Orders and delivery status:")
    print(df[["Order ID", "Delivery Date", "Actual Delivery", "On Time", "Delay (days)"]])

    # Optional: show plot if implemented
    # plot_delivery_status(df)
else:
    print("❌ Failed to load the Excel file.")
