import matplotlib.pyplot as plt
import os

# Bar chart: number of orders on time vs late
def plot_delivery_status(df):
    counts = df["On Time"].value_counts()
    labels = ["On Time", "Late"]
    values = [counts.get(True, 0), counts.get(False, 0)]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=["green", "red"])
    plt.title("Order Delivery Status")
    plt.xlabel("Delivery")
    plt.ylabel("Number of Orders")

    for i, value in enumerate(values):
        plt.text(i, value + 0.2, str(value), ha="center")

    plt.tight_layout()
    plt.show()


# Horizontal bar chart: delay in days for late orders
def plot_delivery_delay(df, save=False, filename="output/delay_chart.png"):
    delayed = df[df["Delay (days)"] > 0]

    if delayed.empty:
        print("✅ All orders were delivered on time. No delay to show.")
        return

    order_ids = delayed["Order ID"]
    delays = delayed["Delay (days)"]

    plt.figure(figsize=(8, 4))
    plt.barh(order_ids, delays, color="orange")
    plt.xlabel("Delay in days")
    plt.ylabel("Order ID")
    plt.title("Orders with Delivery Delay")
    plt.tight_layout()

    if save:
        os.makedirs("output", exist_ok=True)
        plt.savefig(filename)
        plt.close()
        print(f"📸 Chart saved as image: {filename}")
    else:
        plt.show()
