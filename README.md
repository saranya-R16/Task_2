# Dataset Explorer Tool

## Objective

This project automatically explores a CSV dataset using Python and Pandas. It loads the dataset, analyzes its structure, identifies missing values, generates summary statistics, and detects outliers using the IQR method.

## Features

* Load a CSV dataset
* Display dataset shape
* Display column names and data types
* Show the first 5 rows of data
* Detect missing values and percentages
* Generate summary statistics for numeric columns
* Detect outliers using the IQR method

## Requirements

* Python 3.x
* Pandas

## Installation

```bash
pip install pandas
```

## Run the Project

```bash
python explorer.py
```

## Dataset Used

Titanic Dataset (CSV)

## Sample Results

### Dataset Shape

* Rows: 891
* Columns: 12

### Missing Values

* Age: 177
* Cabin: 687
* Embarked: 2

### Outliers Detected

* Age: 11
* SibSp: 46
* Parch: 213
* Fare: 116

## Project Structure

Task_2/
│
├── explorer.py
├── titanic.csv
└── README.md

## Author

Saranya R
