import pandas as pd

def kpis(data):
    return {"learners": data["UserID"].nunique(), "enrollments": len(data), "courses": data["CourseID"].nunique(), "revenue": data["Amount"].sum()}

def course_popularity(data):
    return data.groupby(["CourseID", "CourseName"], as_index=False).agg(Enrollments=("TransactionID", "count"), Revenue=("Amount", "sum")).sort_values("Enrollments", ascending=False)

def demographic_summary(data, column):
    return data.groupby(column, dropna=False).agg(Learners=("UserID", "nunique"), Enrollments=("TransactionID", "count"), Revenue=("Amount", "sum")).reset_index()

def monthly_enrollments(data):
    return data.assign(Month=data["EnrollmentDate"].dt.to_period("M").astype(str)).groupby("Month", as_index=False).agg(Enrollments=("TransactionID", "count"), Revenue=("Amount", "sum"))

