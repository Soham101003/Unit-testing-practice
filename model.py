import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy data: [area, bedrooms]
X = np.array([[1000, 2], [1500, 3], [2000, 4], [2500, 4]])
y = np.array([200000, 300000, 400000, 500000])

model = LinearRegression()
model.fit(X, y)
joblib.dump(model, "model.pkl")
