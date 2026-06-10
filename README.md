# Dataset Explorer Tool

## Overview

Dataset Explorer Tool is a Python-based data analysis project that automatically explores a CSV dataset and provides useful insights about its structure and quality.

The tool loads a dataset, inspects its columns and data types, identifies missing values, generates summary statistics, detects outliers using the IQR method, and visualizes numeric data using histograms.

## Features

* Load CSV datasets using Pandas
* Display dataset shape
* Display column names and data types
* Show the first 5 rows of the dataset
* Detect missing values and percentages
* Generate summary statistics for numeric columns
* Detect outliers using the IQR (Interquartile Range) method
* Visualize numerical columns using histograms

## Technologies Used

* Python 3
* Pandas
* Matplotlib

## Installation

Install the required libraries:

```bash id="p4ls7f"
pip install pandas matplotlib
```

## How to Run

1. Place the dataset file (`titanic.csv`) in the project folder.
2. Open the terminal in VS Code.
3. Run:

```bash id="8rfc8v"
python explorer.py
```

## Dataset Used

Titanic Dataset (CSV)

The dataset contains passenger information such as age, gender, passenger class, ticket fare, and survival status.

## Analysis Performed

### Dataset Inspection

* Dataset shape
* Column names
* Data types
* First 5 rows

### Missing Value Analysis

* Count of missing values
* Percentage of missing values

### Statistical Summary

* Mean
* Median
* Standard Deviation
* Minimum Value
* Maximum Value

### Outlier Detection

* IQR (Interquartile Range) Method

### Data Visualization

* Histogram for each numeric column
* Distribution analysis of numerical features

## Sample Output

### Dataset Shape

* Rows: 891
* Columns: 12

### Missing Values

| Column   | Missing Values |
| -------- | -------------- |
| Age      | 177            |
| Cabin    | 687            |
| Embarked | 2              |

### Outliers Detected

| Column | Outliers |
| ------ | -------- |
| Age    | 11       |
| SibSp  | 46       |
| Parch  | 213      |
| Fare   | 116      |

## Project Structure

```text id="djjlwm"
Task_2/
├── explorer.py
├── titanic.csv
└── README.md
```

## Repository Link

Repository: https://github.com/saranya-R16/Task_2

## Future Improvements

* Add box plots for better outlier visualization
* Export analysis results to CSV or Excel
* Support multiple dataset formats
* Create an interactive dashboard using Streamlit

## License

This project is licensed under the MIT License and is intended for educational and learning purposes.

## Author

Saranya R

GitHub: https://github.com/saranya-R16
