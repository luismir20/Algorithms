import numpy as np
import statsmodels.api as sm

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])  # Independent variable (feature)
Y = np.array([2, 4, 5, 4, 5, 4 ,3 ,3 ,2 ,1 ,1 ,1 ,0.5 ,0.5 ,0.5 ,0.4 ,0.4 ,0.3 ,0.2 ,0.1])  # Dependent variable (target)

X = sm.add_constant(X)

model = sm.OLS(Y, X)

results = model.fit()

print(results.summary())

intercept, slope = results.params

print("Intercept (c):", intercept)
print("Slope (m):", slope)

predicted_Y = results.predict(X)
print("Predicted values:", predicted_Y)
