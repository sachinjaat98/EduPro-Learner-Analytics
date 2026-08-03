import pandas as pd
from .utils import RAW_DIR, PROCESSED_DIR, ensure_directories

def load_raw_data():
    return tuple(pd.read_csv(RAW_DIR / name) for name in ("Users.csv", "Courses.csv", "Transactions.csv"))

def clean_and_merge(users, courses, transactions):
    users = users.drop_duplicates("UserID").copy()
    courses = courses.drop_duplicates("CourseID").copy()
    transactions = transactions.drop_duplicates("TransactionID").copy()

    users["Age"] = pd.to_numeric(users["Age"], errors="coerce")
    transactions["EnrollmentDate"] = pd.to_datetime(transactions["EnrollmentDate"], errors="coerce")
    transactions["Amount"] = pd.to_numeric(transactions["Amount"], errors="coerce").fillna(0)

    merged = transactions.merge(users, on="UserID", how="left", validate="many_to_one").merge(
        courses, on="CourseID", how="left", validate="many_to_one"
    )

    merged = merged.rename(columns={
        "Category": "CourseCategory",
        "Level": "CourseLevel",
        "EnrollmentDate": "TransactionDate"
    })

    merged["AgeGroup"] = pd.cut(
        merged["Age"],
        [0, 17, 25, 35, 50, 120],
        labels=["Under 18", "18-25", "26-35", "36-50", "51+"],
    )

    return merged

def build_processed_data(output=None):
    ensure_directories()
    merged = clean_and_merge(*load_raw_data())
    merged.to_csv(output or PROCESSED_DIR / "merged_data.csv", index=False)
    return merged

if __name__ == "__main__":
    print(f"Wrote {len(build_processed_data())} merged records")

