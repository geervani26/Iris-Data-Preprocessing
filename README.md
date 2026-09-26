# Iris Dataset - Data Preprocessing and Exploratory Data Analysis

## 📌 Project Overview

This project focuses on cleaning, preprocessing, and exploring the Iris dataset using Python.

The dataset contains measurements of iris flowers from three different species:

- Setosa
- Versicolor
- Virginica

The project demonstrates important data preprocessing techniques such as checking for missing values, checking duplicate records, encoding categorical data, and normalizing numerical features.

Exploratory Data Analysis (EDA) was also performed to understand the patterns and relationships within the dataset.

---

## 🎯 Objectives

- Load and inspect the Iris dataset.
- Check and clean the dataset.
- Identify missing values.
- Check for duplicate records.
- Identify invalid values.
- Select relevant features.
- Encode categorical data.
- Normalize numerical features.
- Perform Exploratory Data Analysis.
- Analyze relationships between features.
- Save the processed dataset.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Visual Studio Code

---

## 📂 Dataset Information

The dataset contains 150 records and 5 columns.

### Features

| Feature      | Description                |
|--------------|----------------------------|
| sepal_length | Length of the sepal        |
| sepal_width  | Width of the sepal         |
| petal_length | Length of the petal        |
| petal_width  | Width of the petal         |
| species      | Species of the iris flower |

The dataset contains three species:

- Setosa
- Versicolor
- Virginica

Each species contains 50 samples.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Inspected the dataset structure and dimensions.
3. Checked for missing values.
4. Checked for duplicate records.
5. Checked numerical features for invalid values.
6. Selected the relevant numerical features.
7. Separated features and target variable.
8. Applied Label Encoding to the species column.
9. Applied Min-Max Scaling to numerical features.
10. Verified the processed dataset.
11. Saved the processed dataset as `iris_processed.csv`.

### Missing Values

The dataset was checked for missing values. No missing values were found.

### Label Encoding

The species values were converted into numerical values:

| Species    | Encoded Value |
|------------|---------------|
| Setosa     | 0             |
| Versicolor | 1             |
| Virginica  | 2             |

### Normalization

Min-Max Scaling was applied to the four numerical features so that their values were transformed to a range between 0 and 1.

---

## 📊 Exploratory Data Analysis

The following EDA techniques were performed:

- Species distribution analysis
- Descriptive statistical analysis
- Histograms
- Box plots
- Feature comparison by species
- Scatter plot analysis
- Correlation analysis
- Correlation heatmap

These visualizations were used to understand feature distributions, relationships, and differences between the three species.

---

## 📈 EDA Observations

- The dataset contains an equal number of samples for each species.
- The numerical features have different measurement ranges before normalization.
- Histograms were used to understand the distribution of the numerical features.
- Box plots were used to understand the spread of the features and identify potential outliers.
- Scatter plots were used to visualize relationships between numerical features.
- Correlation analysis was used to understand relationships among the numerical features.
- The four numerical features were successfully normalized between 0 and 1.

---

## 📁 Project Files


Iris-Data-Preprocessing/
│
├── iris_dataset.csv
├── iris_processed.csv
├── iris_preprocessing.ipynb
└── README.md
---

## 👩‍💻 Author

Geervani Nandi Mangalam

GitHub: https://github.com/geervani26
