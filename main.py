print("AI Student Performance Predictor")
print("--------------------------------")

name = input("Enter student name: ")
hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_score = float(input("Enter previous exam score: "))

# Simple prediction logic
score = (
    hours * 5
    + attendance * 0.4
    + previous_score * 0.5
)

if score >= 100:
    result = "Excellent"
elif score >= 75:
    result = "Good"
elif score >= 50:
    result = "Average"
else:
    result = "Needs Improvement"

print("\nPrediction Result")
print("-----------------")
print("Student:", name)
print("Predicted Performance:", result)