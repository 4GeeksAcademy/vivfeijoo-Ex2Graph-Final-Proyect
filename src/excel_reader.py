import pandas as pd

# This function reads the Excel file and adds columns for delay analysis
def read_excel(file_name):
    path = f"data/{file_name}"  # ✅ This matches the variable name from the function

    try:
        # Load the Excel file
        df = pd.read_excel(path)

        # Convert both columns to date format
        df["Delivery Date"] = pd.to_datetime(df["Delivery Date"])
        df["Actual Delivery"] = pd.to_datetime(df["Actual Delivery"])

        # Add a column to check if delivery was on time
        df["On Time"] = df["Actual Delivery"] <= df["Delivery Date"]

        # Calculate the delay in days (0 if not late)
        df["Delay (days)"] = (df["Actual Delivery"] - df["Delivery Date"]).dt.days
        df["Delay (days)"] = df["Delay (days)"].apply(lambda x: x if x > 0 else 0)

        print("✅ Excel file read and processed successfully.")
        return df

    except Exception as e:
        print("❌ Error reading Excel file:", e)
        return None

