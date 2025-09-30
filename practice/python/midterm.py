import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example: Predicting the sine of an angle (trigonometry helper)

# Generate training data (angles in degrees and their sine values)
angles_deg = np.linspace(0, 360, 100)
angles_rad = np.deg2rad(angles_deg)
sine_values = np.sin(angles_rad)

# Reshape for sklearn
X = angles_deg.reshape(-1, 1)
y = sine_values

# Train a simple linear regression model (for demonstration)
model = LinearRegression()
model.fit(X, y)

# Predict sine for a new angle
def predict_sine(angle_deg):
    return model.predict(np.array([[angle_deg]]))[0]

# Example usage
angle = 45
predicted_sine = predict_sine(angle)
print(f"Predicted sine({angle}°): {predicted_sine:.3f}")
print(f"Actual sine({angle}°): {np.sin(np.deg2rad(angle)):.3f}")

# Plotting
plt.scatter(angles_deg, sine_values, label='Actual Sine')
plt.plot(angles_deg, model.predict(X), color='red', label='Model Prediction')
plt.xlabel('Angle (degrees)')
plt.ylabel('Sine Value')
plt.legend()
plt.show()