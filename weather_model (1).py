import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("seattle-weather.csv")
print(data.columns)

# Features and target
X = data[['precipitation', 'wind']]
y = data['temp_max']

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction function
def predict_weather(precipitation, wind):
    prediction = model.predict([[precipitation, wind]])
    return round(prediction[0], 2)