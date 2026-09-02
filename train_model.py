import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load the student data
data = pd.read_csv("student_data.csv")

# Convert performance labels into numbers
encoder = LabelEncoder()
data["performance"] = encoder.fit_transform(data["performance"])

# Input features
X = data[["study_hours", "attendance", "previous_score"]]

# Target
y = data["performance"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the ML model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)

print("Model trained successfully!")
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the model
import joblib

joblib.dump(model, "student_performance_model.pkl")
joblib.dump(encoder, "performance_encoder.pkl")

print("Model saved successfully!")