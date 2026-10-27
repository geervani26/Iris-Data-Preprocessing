import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Step 1: Locate the project folder and dataset
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "iris_dataset.csv"
MODEL_PATH = BASE_DIR / "iris_model.joblib"


# Step 2: Load the dataset
print("Loading the Iris dataset...")

df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)
print("\nAvailable columns:")
print(df.columns.tolist())


# Step 3: Prepare the data
df.columns = df.columns.str.strip()

# Remove rows containing missing values
df = df.dropna().copy()

# Identify the target column
possible_targets = ["species", "target", "class", "variety"]
target_column = next(
    (column for column in df.columns
     if column.lower() in possible_targets),
    None
)

if target_column is None:
    raise ValueError(
        "Could not identify the target column. "
        "Check the column names in iris_dataset.csv."
    )

# Select the four input features
feature_columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

# Handle column names containing spaces or different capitalization
column_lookup = {column.lower(): column for column in df.columns}

missing_features = [
    feature for feature in feature_columns
    if feature not in column_lookup
]

if missing_features:
    raise ValueError(
        f"Missing required feature columns: {missing_features}. "
        "Check the column names in iris_dataset.csv."
    )

actual_features = [column_lookup[name] for name in feature_columns]

X = df[actual_features]
y = df[target_column]

print("\nInput features:", actual_features)
print("Target column:", target_column)
print("Number of samples:", len(df))
print("Species/classes:", sorted(y.astype(str).unique()))


# Step 4: Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# Step 5: Build and train the machine learning pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])

print("\nTraining the Logistic Regression model...")

model.fit(X_train, y_train)


# Step 6: Evaluate the trained model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel training completed!")
print(f"Test accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))


# Step 7: Save the complete trained pipeline
joblib.dump(model, MODEL_PATH)

print("\nTrained model saved successfully!")
print("Saved model location:", MODEL_PATH)