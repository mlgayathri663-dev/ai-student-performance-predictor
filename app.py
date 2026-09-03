import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_performance_model.pkl")
encoder = joblib.load("performance_encoder.pkl")

# Page settings
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# Header
st.title("🎓 AI Student Performance Predictor")
st.write(
    "An AI-powered application for predicting and analyzing student academic performance."
)

st.divider()

# ---------------- SINGLE STUDENT ----------------

st.header("🎯 Single Student Prediction")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    hours = st.number_input(
        "Study Hours Per Day",
        min_value=0.0,
        max_value=24.0,
        value=5.0
    )

with col2:
    attendance = st.number_input(
        "Attendance Percentage",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    previous_score = st.number_input(
        "Previous Exam Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

if st.button("🎯 Predict Performance", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter the student name.")

    else:
        input_data = pd.DataFrame({
            "study_hours": [hours],
            "attendance": [attendance],
            "previous_score": [previous_score]
        })

        prediction = model.predict(input_data)
        performance = encoder.inverse_transform(prediction)[0]

        st.subheader("📊 Prediction Result")

        st.success(f"Performance: {performance}")
        st.info(f"Student: {name}")

        if performance == "Excellent":
            st.write(
                "🌟 Recommendation: Excellent performance. Keep up the good work!"
            )

        elif performance == "Good":
            st.write(
                "👍 Recommendation: Good performance. Continue regular study and practice."
            )

        elif performance == "Average":
            st.write(
                "📚 Recommendation: Encourage more study time and regular revision."
            )

        else:
            st.write(
                "⚠️ Recommendation: Student may need additional academic support."
            )

st.divider()

# ---------------- MULTIPLE STUDENTS ----------------

st.header("📁 Multiple Student Analysis")

st.write(
    "Upload a CSV file to analyze the performance of multiple students."
)

uploaded_file = st.file_uploader(
    "Upload Student CSV",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    required_columns = [
        "name",
        "study_hours",
        "attendance",
        "previous_score"
    ]

    if all(column in data.columns for column in required_columns):

        predictions = model.predict(
            data[
                [
                    "study_hours",
                    "attendance",
                    "previous_score"
                ]
            ]
        )

        data["prediction"] = encoder.inverse_transform(predictions)

        st.subheader("📋 Student Prediction Results")

        st.dataframe(
            data,
            use_container_width=True
        )

        # ---------------- DASHBOARD ----------------

        st.subheader("📈 Performance Dashboard")

        total_students = len(data)

        excellent = (
            data["prediction"] == "Excellent"
        ).sum()

        good = (
            data["prediction"] == "Good"
        ).sum()

        average = (
            data["prediction"] == "Average"
        ).sum()

        needs_improvement = (
            data["prediction"] == "Needs Improvement"
        ).sum()

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("👨‍🎓 Total", total_students)
        col2.metric("🌟 Excellent", excellent)
        col3.metric("👍 Good", good)
        col4.metric("📚 Average", average)
        col5.metric("⚠️ Needs Improvement", needs_improvement)

        # Chart
        chart_data = pd.DataFrame({
            "Performance": [
                "Excellent",
                "Good",
                "Average",
                "Needs Improvement"
            ],
            "Students": [
                excellent,
                good,
                average,
                needs_improvement
            ]
        })

        st.bar_chart(
            chart_data.set_index("Performance")
        )

        # Download report
        csv = data.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Prediction Report",
            data=csv,
            file_name="student_performance_predictions.csv",
            mime="text/csv",
            use_container_width=True
        )

    else:

        st.error(
            "CSV must contain: name, study_hours, attendance, previous_score"
        )

st.divider()

st.caption(
    "AI Student Performance Predictor | Python • Machine Learning • Streamlit"
)