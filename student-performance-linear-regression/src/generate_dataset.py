"""Generate a realistic student performance dataset.

The relationship between features and final marks is positive but noisy,
so the dataset does not produce a perfect correlation.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

n = 200

study_hours = rng.uniform(1, 10, n)               # hours per day
attendance = rng.uniform(50, 100, n)              # percentage
previous_marks = rng.uniform(30, 95, n)           # marks out of 100

# Final marks depend positively on all three features, plus noise
final_marks = (
    0.35 * study_hours * 3.0
    + 0.25 * attendance
    + 0.45 * previous_marks
    + 2.0
    + rng.normal(0, 7, n)
)

# Clip to realistic range and round to 2 decimals
final_marks = np.clip(final_marks, 30, 100)

study_hours = np.round(study_hours, 1)
attendance = np.round(attendance, 1)
previous_marks = np.round(previous_marks, 1)
final_marks = np.round(final_marks, 1)

df = pd.DataFrame(
    {
        "Study_Hours": study_hours,
        "Attendance_Percentage": attendance,
        "Previous_Marks": previous_marks,
        "Final_Marks": final_marks,
    }
)

df.to_csv(
    r"C:\Users\harsh\OneDrive\Desktop\STUDENT_ML\student-performance-linear-regression\dataset\student_performance.csv",
    index=False,
)
print(df.head())
print("\nShape:", df.shape)
print("\nCorrelation with Final_Marks:")
print(df.corr()["Final_Marks"].round(3))
