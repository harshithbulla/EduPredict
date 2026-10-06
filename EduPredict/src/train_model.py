"""Student Performance Prediction using Linear Regression.

Complete ML pipeline: load data -> clean -> EDA -> split -> train ->
evaluate -> visualize -> save outputs.

NOTE: The ONLY ML algorithm used here is LinearRegression from scikit-learn.
"""

import os
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # save figures without showing a window
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------------------------------------------------------------- paths
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "dataset", "student_performance.csv")
FIG = os.path.join(BASE, "results", "figures")
METRICS = os.path.join(BASE, "results", "metrics")
PRED = os.path.join(BASE, "results", "predictions")
for folder in (FIG, METRICS, PRED):
    os.makedirs(folder, exist_ok=True)

sns.set_style("whitegrid")

# ---------------------------------------------------------------- step 2: load
df = pd.read_csv(DATA)
print("First 5 rows:\n", df.head(), "\n")
print("Last 5 rows:\n", df.tail(), "\n")
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nDescriptive statistics:\n", df.describe().round(2))
print("\nMissing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# data cleaning: drop duplicates / rows with missing values if any
before = len(df)
df = df.drop_duplicates().dropna().reset_index(drop=True)
print(f"Rows before cleaning: {before}, after cleaning: {len(df)}")

# ---------------------------------------------------------------- step 3: EDA
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Final_Marks"], alpha=0.6, color="steelblue")
plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "study_hours_vs_marks.png"), dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance_Percentage"], df["Final_Marks"], alpha=0.6, color="darkorange")
plt.title("Attendance vs Final Marks")
plt.xlabel("Attendance Percentage")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "attendance_vs_marks.png"), dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["Previous_Marks"], df["Final_Marks"], alpha=0.6, color="seagreen")
plt.title("Previous Marks vs Final Marks")
plt.xlabel("Previous Marks")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "previous_marks_vs_final_marks.png"), dpi=150)
plt.close()

plt.figure(figsize=(7, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Student Performance Features")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "correlation_heatmap.png"), dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df["Final_Marks"], bins=15, color="mediumpurple", edgecolor="black")
plt.title("Distribution of Final Exam Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "final_marks_distribution.png"), dpi=150)
plt.close()

# ---------------------------------------------------------------- step 4: features
X = df[["Study_Hours", "Attendance_Percentage", "Previous_Marks"]]
y = df["Final_Marks"]
print("\nFeatures:", list(X.columns))
print("Target: Final_Marks")

# ---------------------------------------------------------------- step 5: split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples:  {len(X_test)}")

# ---------------------------------------------------------------- steps 6-7
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ---------------------------------------------------------------- step 8
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMAE  : {mae:.4f}")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R2   : {r2:.4f}")

with open(os.path.join(METRICS, "model_metrics.txt"), "w") as f:
    f.write("Student Performance Prediction - Model Evaluation Metrics\n")
    f.write("============================================================\n")
    f.write(f"Mean Absolute Error (MAE) : {mae:.4f}\n")
    f.write(f"Mean Squared Error (MSE)  : {mse:.4f}\n")
    f.write(f"Root Mean Squared Error   : {rmse:.4f}\n")
    f.write(f"R2 Score                  : {r2:.4f}\n")

metrics_df = pd.DataFrame(
    {
        "Metric": ["MAE", "MSE", "RMSE", "R2 Score"],
        "Value": [round(mae, 4), round(mse, 4), round(rmse, 4), round(r2, 4)],
    }
)
metrics_df.to_csv(os.path.join(METRICS, "model_metrics.csv"), index=False)

# ---------------------------------------------------------------- step 9
print(f"\nIntercept: {model.intercept_:.4f}")
for name, coef in zip(X.columns, model.coef_):
    print(f"Coefficient of {name}: {coef:.4f}")

# ---------------------------------------------------------------- step 10
results = pd.DataFrame(
    {
        "Actual_Final_Marks": y_test.values,
        "Predicted_Final_Marks": np.round(y_pred, 2),
        "Prediction_Error": np.round(y_test.values - y_pred, 2),
    }
)
results.to_csv(os.path.join(PRED, "test_predictions.csv"), index=False)
print("\nSample predictions:\n", results.head(10).to_string(index=False))

# ---------------------------------------------------------------- step 11
plt.figure(figsize=(7, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color="royalblue")
lims = [min(y_test.min(), y_pred.min()) - 5, max(y_test.max(), y_pred.max()) + 5]
plt.plot(lims, lims, "r--", label="Ideal (y = x)")
plt.title("Actual vs Predicted Final Marks")
plt.xlabel("Actual Final Marks")
plt.ylabel("Predicted Final Marks")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(FIG, "actual_vs_predicted.png"), dpi=150)
plt.close()

residuals = y_test.values - y_pred
plt.figure(figsize=(8, 5))
plt.scatter(y_pred, residuals, alpha=0.7, color="crimson")
plt.axhline(0, color="black", linestyle="--")
plt.title("Residual Analysis")
plt.xlabel("Predicted Final Marks")
plt.ylabel("Residuals (Actual - Predicted)")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "residual_plot.png"), dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
bars = plt.bar(["MAE", "RMSE", "R2 Score"], [mae, rmse, r2],
               color=["steelblue", "darkorange", "seagreen"])
for bar, val in zip(bars, [mae, rmse, r2]):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
             f"{val:.2f}", ha="center", va="bottom")
plt.title("Model Performance Metrics")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig(os.path.join(FIG, "model_metrics.png"), dpi=150)
plt.close()

# ---------------------------------------------------------------- step 12
def predict_marks(study_hours, attendance, previous_marks):
    """Predict final marks using the trained Linear Regression model."""
    sample = pd.DataFrame(
        [[study_hours, attendance, previous_marks]],
        columns=["Study_Hours", "Attendance_Percentage", "Previous_Marks"],
    )
    return float(model.predict(sample)[0])

sample = predict_marks(6, 85, 70)
print(f"\nSample Prediction -> Study=6, Attendance=85, Previous=70 : {sample:.2f}")
print("\nPipeline complete. All outputs saved.")
