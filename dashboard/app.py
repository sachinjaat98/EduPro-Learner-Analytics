import streamlit as st
from utils import load_data, apply_filters

st.set_page_config(
    page_title="EduPro Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduPro Analytics Dashboard")

st.markdown("""
### Learner Demographics and Course Enrollment Behavior Analysis

This dashboard provides interactive insights into:

- Learner demographics
- Enrollment behavior
- Course popularity
- Learning preferences
""")

df = load_data()

df = apply_filters(df)

st.divider()

# KPIs

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Learners",
        df["UserID"].nunique()
    )

with col2:
    st.metric(
        "Enrollments",
        len(df)
    )

with col3:
    st.metric(
        "Courses",
        df["CourseID"].nunique()
    )

with col4:
    st.metric(
        "Average Age",
        round(df["Age"].mean(),1)
    )

st.divider()

st.info(
    "Use the navigation panel on the left to explore detailed analyses."
)