import pandas as pd

# ==========================================
# TASK 1 - DATA CLEANING & PREPROCESSING
# ==========================================

# Load dataset
df = pd.read_csv("Task1_Customer_Data.csv")

print("========== ORIGINAL DATA ==========")
print(df)

print("\n========== ORIGINAL INFORMATION ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print("Duplicate rows:", df.duplicated().sum())


# ==========================================
# 1. REMOVE DUPLICATE RECORDS
# ==========================================

df = df.drop_duplicates()


# ==========================================
# 2. HANDLE MISSING NUMERIC VALUES
# ==========================================

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Income"] = df["Income"].fillna(df["Income"].median())

df["PurchaseAmount"] = df["PurchaseAmount"].fillna(
    df["PurchaseAmount"].median()
)


# ==========================================
# 3. STANDARDIZE GENDER
# ==========================================

df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "male": "Male",
    "F": "Female",
    "female": "Female"
})


# ==========================================
# 4. STANDARDIZE CITY NAMES
# ==========================================

df["City"] = df["City"].replace({
    "Bangalore": "Bengaluru",
    "Mysore": "Mysuru"
})


# ==========================================
# 5. CONVERT PURCHASE DATE
# ==========================================

df["PurchaseDate"] = pd.to_datetime(
    df["PurchaseDate"],
    format="mixed",
    dayfirst=False,
    errors="coerce"
)

# ==========================================
# 6. CORRECT DATA TYPES
# ==========================================

df["CustomerID"] = df["CustomerID"].astype(int)

df["Age"] = df["Age"].astype(int)

df["Income"] = df["Income"].astype(float)

df["PurchaseAmount"] = df["PurchaseAmount"].astype(float)


# ==========================================
# FINAL CHECK
# ==========================================

print("\n========== CLEANED DATA ==========")
print(df)

print("\n========== CLEANED INFORMATION ==========")
df.info()

print("\n========== REMAINING MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== REMAINING DUPLICATES ==========")
print(df.duplicated().sum())

print("\n========== FINAL SHAPE ==========")
print(df.shape)

print("\n========== GENDER VALUES ==========")
print(df["Gender"].value_counts())

print("\n========== CITY VALUES ==========")
print(df["City"].value_counts())


# ==========================================
# SAVE CLEANED DATASET
# ==========================================

df.to_csv("cleaned_customer_data.csv", index=False)

print("\n==========================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("Saved file: cleaned_customer_data.csv")
print("==========================================")