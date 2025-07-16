import matplotlib.pyplot as plt

def plot_delivery_status(df):
    # Count how many orders were on time and late
    delivery_counts = df["On Time"].value_counts()

    # Rename labels for better understanding
    labels = ["On Time", "Late"]
    values = [
        delivery_counts.get(True, 0),
        delivery_counts.get(False, 0)
    ]

    # Create a bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=["green", "red"])
    plt.title("Order Delivery Status")
    plt.xlabel("Delivery")
    plt.ylabel("Number of Orders")

    # Show values on top of bars
    for i, value in enumerate(values):
        plt.text(i, value + 0.2, str(value), ha="center")

    # Show the plot
    plt.tight_layout()
    plt.show()
