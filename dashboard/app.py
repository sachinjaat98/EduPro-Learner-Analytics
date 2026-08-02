from pathlib import Path
import sys
import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.analysis import kpis, course_popularity, demographic_summary, monthly_enrollments
from src.visualization import course_bar, demographic_bar, monthly_line
from src.preprocessing import build_processed_data

st.set_page_config(page_title="EduPro Learner Analytics", page_icon="📚", layout="wide")
st.title("📚 EduPro Learner Analytics")
st.caption("Explore learner demographics, enrollment behavior, course demand, and revenue.")
data_path = Path(__file__).resolve().parents[1] / "data" / "processed" / "merged_data.csv"
data = pd.read_csv(data_path, parse_dates=["EnrollmentDate"]) if data_path.exists() else build_processed_data()

filters = st.sidebar.multiselect("Gender", sorted(data["Gender"].dropna().unique()), default=sorted(data["Gender"].dropna().unique()))
filtered = data[data["Gender"].isin(filters)]
metrics = kpis(filtered)
cols = st.columns(4)
for col, (label, value) in zip(cols, [("Learners", metrics["learners"]), ("Enrollments", metrics["enrollments"]), ("Courses", metrics["courses"]), ("Revenue", f"₹{metrics['revenue']:,.0f}")]):
    col.metric(label, value)

left, right = st.columns(2)
left.plotly_chart(course_bar(course_popularity(filtered)), use_container_width=True)
right.plotly_chart(demographic_bar(demographic_summary(filtered, "AgeGroup"), "AgeGroup"), use_container_width=True)
st.plotly_chart(monthly_line(monthly_enrollments(filtered)), use_container_width=True)
st.subheader("Course summary")
st.dataframe(course_popularity(filtered), use_container_width=True, hide_index=True)

