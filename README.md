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




---

# Week 3 – Unsupervised Learning & Model Evaluation

## Overview

In Week 3, the Week 2 supervised machine learning project was extended with unsupervised learning techniques, dimensionality reduction, advanced model evaluation, and hyperparameter tuning.

The same Iris dataset was used to demonstrate the progression from supervised learning to unsupervised learning and advanced model evaluation techniques.

## Objectives

- Understand K-Means Clustering.
- Understand Hierarchical Clustering.
- Learn dimensionality reduction using PCA.
- Evaluate clustering using Silhouette Score.
- Understand and implement Cross-Validation.
- Generate and interpret a Confusion Matrix.
- Calculate Precision, Recall and F1-Score.
- Evaluate multiclass classification using ROC-AUC.
- Perform hyperparameter tuning using GridSearchCV.
- Compare original and tuned models.

## Unsupervised Learning

### 1. K-Means Clustering

K-Means clustering was applied to the four numerical Iris features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The features were standardized before clustering.

The Elbow Method was used to examine different values of K, and three clusters were selected for the Iris dataset.

### 2. Hierarchical Clustering

Hierarchical Clustering was implemented using the Ward linkage method.

A dendrogram was created to visualize the hierarchical relationships between observations.

The resulting clusters were evaluated using the Silhouette Score.

### 3. Clustering Evaluation

K-Means and Hierarchical Clustering were compared using Silhouette Scores to evaluate cluster quality.

## Dimensionality Reduction

### Principal Component Analysis (PCA)

PCA was used to reduce the four-dimensional standardized Iris dataset to two principal components.

The two-dimensional representation was used to visualize the data and K-Means cluster assignments.

## Advanced Model Evaluation

The Logistic Regression model was further evaluated using:

- 5-Fold Cross-Validation
- Confusion Matrix
- Accuracy
- Precision
- Recall
- F1-Score
- Multiclass ROC-AUC

Cross-validation was used to evaluate model performance across multiple data splits.

## Hyperparameter Tuning

GridSearchCV was used to tune the Logistic Regression model.

Different values of the regularization parameter `C` were tested using 5-fold cross-validation.

The best parameter configuration was selected and the tuned model was compared with the original Logistic Regression model.

## Week 3 Workflow


Iris Dataset
      ↓
Feature Preparation
      ↓
Feature Standardization
      ↓
K-Means Clustering
      ↓
Hierarchical Clustering
      ↓
Silhouette Score Evaluation
      ↓
PCA Dimensionality Reduction
      ↓
Cross-Validation
      ↓
Classification Evaluation
      ↓
ROC-AUC Evaluation
      ↓
Hyperparameter Tuning
      ↓
Final Model Comparison


# Week 4: AI Project Deployment & Capstone

## Project Title
Iris Flower Classification — End-to-End Machine Learning Application

## Overview
Week 4 extends the Iris machine learning project by integrating model training, model serialization, a Flask application, and a web-based prediction interface. Users can enter four flower measurements and receive a predicted Iris species.

## Objectives
- Train and evaluate a machine learning classification model.
- Save the trained model using Joblib.
- Build a Flask web application.
- Develop a REST-style prediction API that accepts JSON input.
- Create a user-friendly HTML interface.
- Test predictions and validate API inputs.
- Prepare the project for deployment and documentation.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Flask
- Joblib
- HTML and CSS
- JavaScript
- Visual Studio Code

## Dataset
The Iris dataset contains 150 samples, four numerical features, and three flower species:
- Setosa
- Versicolor
- Virginica

The input features are sepal length, sepal width, petal length, and petal width.

## Model Training and Evaluation
A Logistic Regression model was trained using an 80:20 train-test split.

Recorded results:
- Training samples: 120
- Testing samples: 30
- Test accuracy: 93.33%

The model's performance was evaluated using accuracy, precision, recall, and F1-score.

## Model Serialization
The trained machine learning pipeline is saved as:

`iris_model.joblib`

Joblib allows the Flask application to load the trained model without retraining it every time the application starts.

## Application Features
- Four input fields for flower measurements.
- A prediction button.
- A displayed predicted species.
- A Flask prediction endpoint.
- JSON responses from the prediction API.
- Basic input validation and error handling.

## API Endpoint
Method: POST

Endpoint:* `/predict`

Example JSON request:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:
```json
{
  "predicted_species": "setosa",
  "input_measurements": {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }
}
```

## Project Files
- `train_model.py` — trains, evaluates, and saves the model.
- `app.py` — runs the Flask application and prediction API.
- `iris_model.joblib` — serialized trained model.
- `templates/index.html` — web interface.
- `requirements.txt` — Python package dependencies.
- `iris_dataset.csv` — original dataset.
- `iris_ml_models.ipynb` — machine learning experiments from earlier project stages.

## How to Run the Application

1. Install Python.
2. Open the project folder in VS Code.
3. Install the required dependencies:

   `python -m pip install -r requirements.txt`

4. Train and save the model:

   `python train_model.py`

5. Start the Flask application:

   `python app.py`

6. Open the application in your browser:

   `http://127.0.0.1:5000`

## Conclusion
Week 4 demonstrates how a trained machine learning model can be integrated into a web application. The project combines model training, evaluation, serialization, API development, and user interface design. The next stage is to deploy the application to a hosting platform and prepare the final capstone presentation.

## 👩‍💻 Author

Geervani Nandi Mangalam

GitHub: https://github.com/geervani26
