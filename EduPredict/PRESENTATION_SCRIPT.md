# Presentation Script — EduPredict (~5–7 minutes)

**Slide 1 — Title (30 sec):**
Good morning. I am presenting EduPredict: Student Performance Prediction Using Linear Regression. This is my individual AAT project. Here are my project details.

**Slide 2 — Introduction (40 sec):**
Machine Learning lets computers learn patterns from data. My project is supervised learning, because the training data already has answers. Since I predict a number — final marks — it is a regression problem.

**Slide 3 — Problem Statement (30 sec):**
The problem: given a student's study hours, attendance, and previous marks, predict their final exam marks using Linear Regression.

**Slide 4 — Objectives (30 sec):**
My objectives were to prepare a realistic dataset, clean and explore it, train a Linear Regression model, predict marks for unseen students, and evaluate it honestly.

**Slide 5 — Dataset & Features (40 sec):**
The dataset has 200 students. Features: study hours per day (1–10), attendance percentage (50–100), previous marks (30–95). Target is final marks. I split it 160 training and 40 testing with random_state 42.

**Slide 6 — Methodology (40 sec):**
My workflow was: dataset, preprocessing, EDA, feature selection, train-test split, Linear Regression training, prediction, evaluation, visualization, and conclusion.

**Slide 7 — Algorithm (40 sec):**
Linear Regression fits the equation Final_Marks = intercept + coefficients times features. From training, the intercept is -0.3966, and the coefficients are 1.1695 for study hours, 0.3000 for attendance, and 0.4084 for previous marks. All positive — more study, attendance, and prior marks are associated with higher final marks.

**Slide 8 — EDA (40 sec):**
The correlation heatmap shows all three features are positively correlated with final marks, with previous marks being the strongest. The scatter plot of previous marks vs final marks shows a clear positive trend.

**Slide 9 — Model Results (40 sec):**
Test results: MAE 5.66, MSE 47.14, RMSE 6.87, and R² 0.62. So on average predictions differ from real marks by around 6–7 marks, and the three features explain about 62% of the variation in final marks. This is not perfect, but it is a reasonable result.

**Slide 10 — Actual vs Predicted (30 sec):**
In this graph, points close to the red diagonal line are good predictions. Most points cluster around the line with some spread, which matches the RMSE of about 7 marks.

**Slide 11 — Conclusion & Future Scope (30 sec):**
In conclusion, EduPredict gives a simple, interpretable predictor of final marks. Future work can use a bigger real dataset and more features like assignments and sleep.

**Slide 12 — Thank You (10 sec):**
Thank you. I am ready for questions.
