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





---

# Week 2 – Supervised Machine Learning Models

## Project Overview

In Week 2, supervised machine learning models were implemented using the Iris dataset. The main objective was to understand model training, prediction, and evaluation using Scikit-learn.

The project includes both classification and regression experiments.

## Machine Learning Models

### Classification Models

The following classification algorithms were implemented:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. K-Nearest Neighbors (KNN)

### Regression Model

5. Linear Regression

Linear Regression was implemented as a separate regression experiment because the Iris `species` variable is categorical and is therefore not suitable as a regression target.

For the regression task, `petal_length` was used as the continuous target variable.

## Workflow

The Week 2 workflow included:

- Loading the Iris dataset
- Exploring the dataset
- Selecting features and target variables
- Encoding the categorical target
- Splitting data into training and testing sets
- Training machine learning models
- Making predictions
- Evaluating model performance
- Comparing classification model accuracy
- Generating classification reports
- Creating confusion matrices
- Evaluating Linear Regression using regression metrics
- Visualizing actual and predicted values
- Saving model comparison results

## Evaluation Metrics

### Classification

The classification models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### Regression

The Linear Regression model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

## Model Comparison

The classification models were compared using their test-set accuracy.

The comparison results are stored in:

`model_comparison_results.csv`

## Files Added for Week 2

- `iris_ml_models.ipynb` – Jupyter Notebook containing the complete machine
  learning implementation
- `model_comparison_results.csv` – Classification model accuracy results

## Tools and Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- VS Code
- Git and GitHub

## Conclusion

The Week 2 project provided practical experience with supervised machine learning. Multiple classification algorithms were trained and evaluated on the Iris dataset, and their performance was compared using evaluation metrics. A separate Linear Regression experiment demonstrated regression on a continuous numerical target. The project helped demonstrate the complete workflow from data preparation and model training to prediction and evaluation.



## 👩‍💻 Author

Geervani Nandi Mangalam

GitHub: https://github.com/geervani26
