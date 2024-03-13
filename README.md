# Diabetise-Project
Title: Diabetes Prediction Project

Description:
This project focuses on predicting the onset of diabetes using machine learning techniques. The dataset was sourced from Kaggle and underwent extensive preprocessing and analysis to ensure data quality and model effectiveness.

The project pipeline includes the following steps:

Data Exploration: The dataset was thoroughly explored to identify null values, duplicates, and outliers. Descriptive statistics and visualizations were utilized to gain insights into the data.

Data Cleaning: Null values were handled appropriately, and outliers were detected and removed. For columns with outliers, imputation techniques such as mean replacement were applied to maintain data integrity.

Data Transformation: To improve model performance, transformations were applied to ensure that the data conforms to normal distribution assumptions.

Model Building: Several machine learning models including logistic regression, random forest, SVM, and stacking were trained on the preprocessed data. Cross-validation techniques were employed to evaluate model performance, and logistic regression emerged as the best-performing model based on accuracy metrics.

Model Evaluation: A comprehensive classification report was generated for each model, providing insights into precision, recall, and F1-score metrics. This enabled a thorough comparison of model performance.

Deployment: The final model was deployed into a web application using Streamlit, allowing users to interactively predict the likelihood of diabetes onset based on input features.

This project showcases the end-to-end process of developing a predictive model for diabetes onset prediction, from data preprocessing and model training to evaluation and deployment. It serves as a valuable resource for understanding and implementing machine learning techniques in healthcare analytics.

LINK OF STREAMLIT WEBAPP - http://localhost:8501/


