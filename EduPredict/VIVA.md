# VIVA Preparation — EduPredict

## 20 Likely Viva Questions and Answers

**1. What is Machine Learning?**
Machine Learning is a branch of AI where computers learn patterns from data and make predictions without being explicitly programmed for every case.

**2. What type of ML is this?**
Supervised learning, specifically regression.

**3. Why is this supervised learning?**
Because the training data already contains the correct answers — the final marks for each student.

**4. Why is this a regression problem?**
Because the target (Final_Marks) is a continuous number, not a category.

**5. What is Linear Regression?**
It is a supervised algorithm that fits a straight line (or hyperplane) relating the input features to a numeric output.

**6. Why did you choose Linear Regression?**
It is in our syllabus, simple, fast, and easy to interpret. The features appear to have an approximately linear relation with final marks.

**7. What are your input features?**
Study Hours, Attendance Percentage, and Previous Marks.

**8. What is your target variable?**
Final_Marks.

**9. What is train-test split?**
It divides the data into a training set (used to learn) and a test set (used to check performance on unseen data).

**10. Why 80/20?**
80% gives enough data to train; 20% leaves a reasonable sample (40 records) for honest testing.

**11. Why random_state = 42?**
It fixes the random split so we get the same results every time we run the code.

**12. What is MAE?**
Mean Absolute Error — average of the absolute differences between actual and predicted marks. Our MAE = 5.6561.

**13. What is MSE?**
Mean Squared Error — average of the squared errors. Our MSE = 47.1436. It penalizes large errors more.

**14. What is RMSE?**
Root Mean Squared Error — square root of MSE, in the same units as marks. Our RMSE = 6.8661.

**15. What is R²?**
R² is the coefficient of determination — the proportion of variation in the target explained by the features. Ours is 0.6206, i.e. about 62% of the variation is explained.

**16. Why don't you use accuracy?**
Accuracy is for classification problems. For regression we use MAE, MSE, RMSE, and R².

**17. What is a coefficient?**
It tells how much the predicted marks change when that feature increases by 1 unit, keeping other features constant. Ours: Study Hours 1.1695, Attendance 0.3000, Previous Marks 0.4084.

**18. What is the intercept?**
The predicted value when all features are zero. Ours is -0.3966.

**19. What are the limitations?**
Small dataset (200 records), only three features, assumes a linear relationship, and ignores factors like health, stress, and environment.

**20. What would you improve in the future?**
Use a larger real dataset, add more features like assignment marks and sleep patterns, and compare with other syllabus algorithms.
