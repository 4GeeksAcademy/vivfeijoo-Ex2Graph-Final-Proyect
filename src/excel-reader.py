import pandas as pd

def read_excel(filename):
    path = f"../data/{filename}"
    try:
        # Read Excel file
        df = pd.read_excel(path)

        # Convert date columns to datetime format
        df["Delivery Date"] = pd.to_datetime(df["Delivery Date"])
        df["Actual Delivery"] = pd.to_datetime(df["Actual Delivery"])

        # Check if the order was delivered on time
        df["On Time"] = df["Actual Delivery"] <= df["Delivery Date"]

        # Calculate delay in days (0 if on time)
        df["Delay (days)"] = (df["Actual Delivery"] - df["Delivery Date"]).dt.days
        df["Delay (days)"] = df["Delay (days)"].apply(lambda x: x if x > 0 else 0)

        print("✅ Excel file read and processed successfully.")
        return df

    except Exception as e:
        print("❌ Error reading Excel file:", e)
        return None
