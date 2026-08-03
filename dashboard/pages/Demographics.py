import streamlit as st
import plotly.express as px

from utils import load_data, apply_filters

st.title("📊 Learner Demographics")

df = load_data()
df = apply_filters(df)

####################################
# Age Distribution
####################################

fig = px.histogram(
    df,
    x="Age",
    nbins=10,
    title="Age Distribution",
    color_discrete_sequence=["royalblue"]
)

st.plotly_chart(fig, use_container_width=True)

####################################
# Gender
####################################

gender = (
    df["Gender"]
      .value_counts()
      .reset_index()
)

gender.columns = ["Gender","Count"]

fig = px.pie(
    gender,
    values="Count",
    names="Gender",
    title="Gender Distribution"
)

st.plotly_chart(fig, use_container_width=True)

####################################
# Age Groups
####################################

age = (
    df["AgeGroup"]
      .value_counts()
      .sort_index()
      .reset_index()
)

age.columns=["AgeGroup","Enrollments"]

fig = px.bar(
    age,
    x="AgeGroup",
    y="Enrollments",
    color="Enrollments",
    title="Age Group Distribution"
)

st.plotly_chart(fig, use_container_width=True)