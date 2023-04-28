import numpy as np

X = np.array([1, 2, 3, 4, 5])  # Independent variable (feature)
Y = np.array([2, 4, 5, 4, 5])  # Dependent variable (target)

mean_X = np.mean(X)
mean_Y = np.mean(Y)

numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - mean_X) * (Y[i] - mean_Y)
    denominator += (X[i] - mean_X) ** 2

slope = numerator / denominator
intercept = mean_Y - slope * mean_X

print("Slope (m):", slope)
print("Intercept (c):", intercept)

predicted_Y = slope * X + intercept
print("Predicted values:", predicted_Y)
