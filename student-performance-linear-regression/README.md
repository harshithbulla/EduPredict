# Student Performance Prediction Using Linear Regression

## Overview

This is an individual Machine Learning (AAT) project that predicts a student's final examination marks based on three academic factors: study hours, attendance percentage, and previous marks. The only ML algorithm used in this project is **Linear Regression** from scikit-learn.

## Problem Statement

Teachers and students often want an estimate of final exam performance based on current academic behavior. This project builds a simple, interpretable regression model that predicts final marks from:

- Study Hours (per day)
- Attendance Percentage
- Previous / Internal Marks

## Objectives

1. Collect/prepare a realistic student performance dataset.
2. Explore the data and understand feature relationships.
3. Train a Linear Regression model on the data.
4. Predict final exam marks for unseen test data.
5. Evaluate the model using MAE, MSE, RMSE, and R² score.
6. Interpret the model coefficients in a meaningful way.

## Algorithm

**Linear Regression** (`sklearn.linear_model.LinearRegression`)

The model fits a line of the form:

```
Final_Marks = b0 + b1*(Study_Hours) + b2*(Attendance) + b3*(Previous_Marks)
```

## Dataset

- Records: 200 students
- Columns: Study_Hours, Attendance_Percentage, Previous_Marks, Final_Marks
- File: `dataset/student_performance.csv`

## Features

| Feature | Description | Range (approx.) |
|---------|-------------|------------------|
| Study_Hours | Study hours per day | 1 – 10 |
| Attendance_Percentage | Class attendance | 50 – 100 |
| Previous_Marks | Earlier/internal marks | 30 – 95 |

**Target:** Final_Marks (approx. 30 – 100)

## Project Structure

```
student-performance-linear-regression/
├── dataset/
│   └── student_performance.csv
├── notebooks/
│   └── student_performance_prediction.ipynb
├── src/
│   ├── generate_dataset.py
│   └── train_model.py
├── results/
│   ├── figures/
│   ├── metrics/
│   └── predictions/
├── report/
│   └── report.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies Used

- Python 3
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (LinearRegression, metrics, train_test_split)
- Jupyter Notebook

## Methodology

1. Dataset creation
2. Data understanding & cleaning
3. Exploratory Data Analysis (EDA)
4. Feature and target selection
5. Train-test split (80/20, random_state=42)
6. Linear Regression training
7. Prediction on test data
8. Evaluation (MAE, MSE, RMSE, R²)
9. Visualization and interpretation

## Installation

```bash
pip install -r requirements.txt
```

## How to Run

Generate the dataset and run the full pipeline:

```bash
python src/generate_dataset.py
python src/train_model.py
```

Or open the notebook:

```bash
jupyter notebook notebooks/student_performance_prediction.ipynb
```

## Results

Actual results produced by the trained model:

| Metric | Value |
|--------|-------|
| MAE | 5.6561 |
| MSE | 47.1436 |
| RMSE | 6.8661 |
| R² Score | 0.6206 |

Model parameters:

| Parameter | Value |
|-----------|-------|
| Intercept (b0) | -0.3966 |
| Study Hours coefficient | 1.1695 |
| Attendance coefficient | 0.3000 |
| Previous Marks coefficient | 0.4084 |

- Training samples: 160
- Testing samples: 40

## Visualizations

All graphs are saved in `results/figures/`:

- `study_hours_vs_marks.png`
- `attendance_vs_marks.png`
- `previous_marks_vs_final_marks.png`
- `correlation_heatmap.png`
- `final_marks_distribution.png`
- `actual_vs_predicted.png`
- `residual_plot.png`
- `model_metrics.png`

## Sample Prediction

```
Study Hours = 6, Attendance = 85, Previous Marks = 70
Predicted Final Marks = 60.70
```

## Limitations

- Small dataset (200 records).
- Only three input features.
- Assumes a linear relationship between features and marks.
- Does not capture health, stress, study quality, and other real-world factors.

## Future Scope

- Use a larger real-world dataset.
- Add more features such as assignment marks, sleep hours, and study patterns.
- Compare with other syllabus algorithms (e.g., Decision Trees) in future work.

## Conclusion

Linear Regression provides a simple, interpretable way to predict student final marks. The model achieved an R² of about 0.62, meaning the three features explain roughly 62% of the variation in final marks. This is a reasonable result for a simple undergraduate project.
