from pathlib import Path

import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DATA_PATH = Path(r"C:\Users\sachi\OneDrive\Desktop\Edupro\EduPro-Learner-Analytics\data\processed\merged_data.csv")

st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    column_map = {
        "EnrollmentDate": "TransactionDate",
        "Category": "CourseCategory",
        "Level": "CourseLevel",
    }
    df = df.rename(columns=column_map)

    if "TransactionDate" in df.columns:
        df["TransactionDate"] = pd.to_datetime(df["TransactionDate"], errors="coerce")

    if "AgeGroup" not in df.columns and "Age" in df.columns:
        df["AgeGroup"] = pd.cut(
            pd.to_numeric(df["Age"], errors="coerce"),
            [0, 17, 25, 35, 50, 120],
            labels=["Under 18", "18-25", "26-35", "36-50", "51+"],
        )

    for column in ("Gender", "CourseCategory", "CourseLevel", "AgeGroup"):
        if column not in df.columns:
            df[column] = "Unknown"

    return df


@st.cache_data
def load_data():
    df = pd.read_csv(
        PROCESSED_DATA_PATH,
        parse_dates=["TransactionDate"]
    )
    return df


def apply_filters(df):

    age = st.sidebar.multiselect(
        "Age Group",
        sorted(df["AgeGroup"].dropna().unique())
    )

    gender = st.sidebar.multiselect(
        "Gender",
        sorted(df["Gender"].dropna().unique())
    )

    category = st.sidebar.multiselect(
        "Course Category",
        sorted(df["CourseCategory"].dropna().unique())
    )

    level = st.sidebar.multiselect(
        "Course Level",
        sorted(df["CourseLevel"].dropna().unique())
    )

    if age:
        df = df[df["AgeGroup"].isin(age)]

    if gender:
        df = df[df["Gender"].isin(gender)]

    if category:
        df = df[df["CourseCategory"].isin(category)]

    if level:
        df = df[df["CourseLevel"].isin(level)]

    return df
