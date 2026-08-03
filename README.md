# 🎓 EduPro Learner Demographics and Course Enrollment Behavior Analysis

## 📖 Project Overview

This project presents a comprehensive analysis of learner demographics and course enrollment behavior on the **EduPro Online Learning Platform**. The objective is to understand learner characteristics, enrollment trends, and course preferences using Exploratory Data Analysis (EDA) and an interactive Streamlit dashboard.

The analysis provides valuable insights that can help educational platforms make data-driven decisions regarding course development, learner engagement, marketing strategies, and accessibility.

---

## 🎯 Objectives

The project aims to answer the following analytical questions:

- What is the age distribution of learners?
- Which age groups are most active?
- How does enrollment differ by gender?
- Which course categories receive the highest enrollments?
- Which course levels are most preferred?
- How do age groups influence course preferences?
- How do male and female learners differ in course selection?
- What is the average number of courses taken per learner?

---

## 📂 Dataset

The project uses the **EduPro Online Platform** dataset consisting of three primary tables.

### Users

| Column |
|---------|
| UserID |
| UserName |
| Age |
| Gender |

### Courses

| Column |
|---------|
| CourseID |
| CourseName |
| CourseCategory |
| CourseType |
| CourseLevel |

### Transactions

| Column |
|---------|
| TransactionID |
| UserID |
| CourseID |
| TransactionDate |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

---

## 📊 Project Workflow

```text
Raw Dataset
      │
      ▼
Data Cleaning & Preprocessing
      │
      ▼
Data Integration
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Interactive Dashboard
      │
      ▼
Business Insights & Recommendations
```

---

## 📁 Repository Structure

```text
EduPro-Learner-Analytics/
│
├── dashboard/
│   ├── app.py
│   ├── utils.py
│   └── pages/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Preprocessing.ipynb
│   └── 02_EDA.ipynb
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📈 Dashboard Features

The Streamlit dashboard provides:

- Interactive KPI cards
- Learner demographic analysis
- Age-wise enrollment analysis
- Gender distribution
- Course category popularity
- Course level analysis
- Course type analysis
- Top enrolled courses
- Age Group vs Course Category Heatmap
- Gender vs Course Level Comparison
- Monthly enrollment trends
- Interactive filtering

---

## 📊 Key Performance Indicators (KPIs)

- Total Learners
- Total Courses
- Total Enrollments
- Average Learner Age
- Average Courses per Learner
- Most Popular Course Category
- Most Preferred Course Level

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your_username>/EduPro-Learner-Analytics.git
```

Move to the project folder

```bash
cd EduPro-Learner-Analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📷 Dashboard Preview

### Home Dashboard

> Add Screenshot Here

### Learner Demographics

> Add Screenshot Here

### Course Analysis

> Add Screenshot Here

### Behavioral Insights

> Add Screenshot Here

---

## 🔍 Key Findings

- The majority of learners belong to the **18–25** age group.
- Learner participation is balanced across genders.
- Beginner-level courses receive the highest enrollments.
- Certain course categories dominate learner interest.
- Most learners enroll in multiple courses, indicating strong engagement.

---

## 💡 Recommendations

- Expand offerings in high-demand categories.
- Develop personalized learning paths.
- Introduce advanced courses for experienced learners.
- Increase outreach to underrepresented learner segments.
- Improve learner retention through targeted engagement.

---

## 📌 Future Scope

- Predict learner enrollment using Machine Learning.
- Build recommendation systems.
- Analyze learner retention.
- Perform sentiment analysis on learner feedback.
- Deploy the dashboard on Streamlit Community Cloud.

---

## 📜 License

This project is developed for educational and academic purposes.