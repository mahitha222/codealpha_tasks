# ==========================================
# CodeAlpha Internship - Task 1
# Iris Flower Classification
# ==========================================

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Dataset
data = pd.read_csv("Iris (1).csv")

# Display first 5 rows
print("First 5 rows of dataset:\n")
print(data.head())

# 2. Data Preprocessing

# Drop 'Id' column if present
if 'Id' in data.columns:
    data = data.drop(columns=['Id'])

# Features and Target
X = data.drop(columns=['Species'])
y = data['Species']

# 3. Split Dataset (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 5. Make Predictions
y_pred = model.predict(X_test)

# 6. Evaluate Model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 7. Predict New Sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)

print("\nPredicted Species:", prediction[0])
