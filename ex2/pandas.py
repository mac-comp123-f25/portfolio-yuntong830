import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 19, 22],
    "Major": ["Math", "CS", "Physics"]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
avg_age = df["Age"].mean()
print("\nAverage Age:", avg_age)
older_students = df[df["Age"] > 20]
print("\nStudents older than 20:")
print(older_students)