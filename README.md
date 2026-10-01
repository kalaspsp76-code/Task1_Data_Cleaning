# Task 1 – Data Cleaning and Preprocessing

## 📌 Project Overview

This project demonstrates **data cleaning and preprocessing using Python and Pandas**.

The goal is to identify and correct common data-quality problems such as missing values, duplicate records, inconsistent categorical values, and mixed date formats.

---

## 🎯 Objectives

* Load and inspect a CSV dataset
* Identify missing values
* Detect duplicate records
* Handle missing numerical values
* Standardize inconsistent categorical values
* Convert date columns into a proper datetime format
* Verify the quality of the cleaned dataset
* Export the cleaned dataset as a new CSV file

---

## 🗂️ Dataset

The project uses a customer dataset containing the following columns:

| Column           | Description                |
| ---------------- | -------------------------- |
| `CustomerID`     | Unique customer identifier |
| `Name`           | Customer name              |
| `Age`            | Customer age               |
| `Gender`         | Customer gender            |
| `City`           | Customer city              |
| `Income`         | Customer income            |
| `PurchaseAmount` | Amount purchased           |
| `PurchaseDate`   | Date of purchase           |

### Original Dataset

* **Records:** 15
* **Columns:** 8
* **Missing Age:** 1
* **Missing Income:** 1
* **Missing PurchaseAmount:** 1
* **Duplicate records:** 1

---

## 🧹 Data Cleaning Performed

### 1. Missing Values

Missing numerical values were identified and filled using the **median** of the corresponding column.

Affected columns:

* Age
* Income
* PurchaseAmount

### 2. Duplicate Records

One duplicate customer record was detected and removed using Pandas.

### 3. Gender Standardization

Different representations were standardized:

```text
M     → Male
male  → Male
F     → Female
female → Female
```

The final dataset contains only:

```text
Male
Female
```

### 4. City Standardization

Inconsistent city names were standardized:

```text
Bangalore → Bengaluru
Mysore    → Mysuru
```

### 5. Date Conversion

The `PurchaseDate` column contained mixed date formats.

The values were converted into a consistent Pandas datetime format.

### 6. Data Type Correction

Appropriate data types were assigned to:

* CustomerID
* Age
* Income
* PurchaseAmount
* PurchaseDate

---

## 📊 Final Results

| Metric                 | Before Cleaning | After Cleaning |
| ---------------------- | --------------: | -------------: |
| Records                |              15 |             14 |
| Columns                |               8 |              8 |
| Duplicate records      |               1 |              0 |
| Missing Age            |               1 |              0 |
| Missing Income         |               1 |              0 |
| Missing PurchaseAmount |               1 |              0 |
| Missing PurchaseDate   |               0 |              0 |

### Final Dataset

```text
14 records × 8 columns
```

The final dataset contains **0 missing values** and **0 duplicate records**.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **CSV**
* **PowerShell**
* **Git**
* **GitHub**

---

## 📁 Project Structure

```text
Task1_Data_Cleaning/
│
├── data_cleaning.py
├── Task1_Customer_Data.csv
├── cleaned_customer_data.csv
├── README.md
└── Task1_Data_Cleaning_Report.pdf
```

### File Description

**`data_cleaning.py`**
Python program used to inspect, clean, preprocess, and verify the dataset.

**`Task1_Customer_Data.csv`**
Original dataset containing intentional data-quality issues.

**`cleaned_customer_data.csv`**
Final cleaned dataset ready for further analysis.

**`Task1_Data_Cleaning_Report.pdf`**
Project documentation containing the methodology, results, learning outcomes, and conclusion.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/kalaspsp76-code/Task1_Data_Cleaning.git
```

### 2. Open the project directory

```bash
cd Task1_Data_Cleaning
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run the cleaning program

```bash
python data_cleaning.py
```

The program generates:

```text
cleaned_customer_data.csv
```

---

## 📚 Learning Outcomes

Through this project, I learned:

* How to load CSV files using Pandas
* How to inspect datasets
* How to identify missing values
* How to detect and remove duplicates
* How to handle missing numerical data
* How to standardize categorical data
* How to convert date values into datetime format
* How to verify data quality after preprocessing
* How to save and manage cleaned datasets
* How to use Git and GitHub for project version control

---

## 🤖 AI Assistance

AI was used as a learning and development assistant during this project.

It helped with:

* Understanding data-cleaning concepts
* Learning Pandas operations
* Troubleshooting Python and PowerShell errors
* Structuring the preprocessing workflow
* Reviewing the final verification process
* Preparing project documentation

The dataset cleaning and program execution were performed in the local Python environment.

---

## ✅ Project Status

**Completed successfully**

Final dataset:

```text
Rows:             14
Columns:           8
Missing values:    0
Duplicate rows:    0
```

---

## 👨‍💻 Author

**Kala S P**

GitHub: `kalaspsp76-code`

---

⭐ This project demonstrates practical data cleaning and preprocessing using Python and Pandas.
