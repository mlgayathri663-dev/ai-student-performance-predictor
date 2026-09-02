import joblib

# Load the trained model
model = joblib.load("student_performance_model.pkl")
encoder = joblib.load("performance_encoder.pkl")

print("AI Student Performance Predictor")
print("--------------------------------")

name = input("Enter student name: ")
hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous exam score: "))

# Make prediction
prediction = model.predict([[hours, attendance, previous_score]])

# Convert prediction back to text
performance = encoder.inverse_transform(prediction)[0]

print("\nPrediction Result")
print("-----------------")
print("Student:", name)
print("Predicted Performance:", performance)