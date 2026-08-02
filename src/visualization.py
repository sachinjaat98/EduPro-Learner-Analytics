import plotly.express as px

def course_bar(data):
    return px.bar(data, x="CourseName", y="Enrollments", color="Revenue", title="Course popularity", text_auto=True)

def demographic_bar(data, column):
    return px.bar(data, x=column, y="Enrollments", color="Revenue", title=f"Enrollments by {column}")

def monthly_line(data):
    return px.line(data, x="Month", y="Enrollments", markers=True, title="Monthly enrollments")

