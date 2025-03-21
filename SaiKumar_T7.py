import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (replace 'your_dataset.csv' with actual file)
df = pd.read_csv('Student_Performance.csv')

df.head()
# Define independent variables (X) and dependent variable (y)
X = df[['Hours Studied',"Previous Scores"]]  # Replace with actual column names
y = df['Performance Index']  # Replace with actual column name

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Coefficients and intercept
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Scatter plot for actual vs predicted values
plt.scatter(y_test, y_pred, color='blue', label='Actual vs Predicted')

# Plot regression line
x_line = np.linspace(y_test.min(), y_test.max(), 100)
y_line = x_line  # Ideal case where prediction = actual
plt.plot(x_line, y_line, color='red', linestyle='dashed', label='Regression Line')

plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted with Regression Line')
plt.legend()
plt.show()