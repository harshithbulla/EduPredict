# EduPredict
## Student Performance Prediction Using Linear Regression

## Overview

EduPredict is an individual Machine Learning (AAT) project that predicts a student's final examination marks from study hours, attendance percentage, and previous marks. The only ML algorithm used is **Linear Regression** from scikit-learn.

## Problem Statement

Estimate a student's final exam marks based on:

- Study hours per day
- Attendance percentage
- Previous / internal marks

## Objectives

1. Prepare a realistic dataset of 200 students.
2. Explore and clean the data.
3. Train a Linear Regression model.
4. Predict marks for unseen test students.
5. Evaluate using MAE, MSE, RMSE, and R².

## Algorithm

Linear Regression (`sklearn.linear_model.LinearRegression`)

```
Final_Marks = -0.3966 + 1.1695×Study_Hours + 0.3000×Attendance + 0.4084×Previous_Marks
```

## Dataset

- 200 records, 4 columns, all numeric
- No missing values, no duplicates
- File: `dataset/student_performance.csv`

## Features

| Feature | Description |
|---|---|
| Study_Hours | Study hours per day (~1–10) |
| Attendance_Percentage | Attendance (~50–100) |
| Previous_Marks | Previous marks (~30–95) |
| Final_Marks | Target (~30–100) |

## Methodology

Dataset → Preprocessing → EDA → Feature Selection → Train-Test Split (80/20, random_state=42) → Linear Regression Training → Prediction → Evaluation → Visualization → Conclusion

## Project Structure

```
EduPredict/
├── dataset/student_performance.csv
├── notebooks/student_performance_prediction.ipynb
├── src/generate_dataset.py, train_model.py, make_ppt.py
├── results/figures/ (8 graphs)
├── results/metrics/
├── results/predictions/
├── report/report.md
├── presentation/EduPredict_AAT_Presentation.pptx
├── VIVA.md
├── PRESENTATION_SCRIPT.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, python-pptx

## Installation

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python src/generate_dataset.py
python src/train_model.py
python src/make_ppt.py
jupyter notebook notebooks/student_performance_prediction.ipynb
```

## Results

| Metric | Value |
|---|---:|
| MAE | 5.6561 |
| MSE | 47.1436 |
| RMSE | 6.8661 |
| R² Score | 0.6206 |

| Parameter | Value |
|---|---:|
| Intercept | -0.3966 |
| Study Hours coefficient | 1.1695 |
| Attendance coefficient | 0.3000 |
| Previous Marks coefficient | 0.4084 |

Train / Test: 160 / 40 (80/20, random_state=42)

## Visualizations

Saved under `results/figures/`: study hours vs marks, attendance vs marks, previous marks vs final marks, correlation heatmap, final marks distribution, actual vs predicted, residual plot, model metrics.

## Sample Prediction

```
Study Hours = 6, Attendance = 85, Previous Marks = 70
Predicted Final Marks ≈ 60.70
```

## Limitations

Small dataset, only three features, assumes linearity, ignores health/stress/environment.

## Future Scope

Larger real dataset, more features (assignments, sleep, consistency), comparison with other syllabus algorithms.

## Conclusion

EduPredict gives a simple, interpretable Linear Regression model for predicting final marks with honest evaluation (R² ≈ 0.62).
