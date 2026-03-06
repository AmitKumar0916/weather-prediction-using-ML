import streamlit as st
from weather_model import predict_weather

st.title("🌦 Weather Prediction App")

st.write("Enter weather details:")

precipitation = st.number_input("Precipitation", min_value=0.0)
wind = st.number_input("Wind Speed", min_value=0.0)

if st.button("Predict Temperature"):
    result = predict_weather(precipitation, wind)
    st.success(f"Predicted Max Temperature: {result} °C")


























# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from weather_model import predict_weather

# st.title("🌦 Weather Prediction App")

# # Load dataset
# data = pd.read_csv("seattle-weather.csv")

# st.subheader("📁 Dataset Preview")
# st.write(data.head())

# st.subheader("📊 Temperature Graph")
# fig, ax = plt.subplots()
# ax.plot(data["temp_max"])
# st.pyplot(fig)

# st.subheader("🔮 Predict Temperature")

# precipitation = st.number_input("Precipitation", min_value=0.0)
# wind = st.number_input("Wind Speed", min_value=0.0)

# if st.button("Predict Temperature"):
#     result = predict_weather(precipitation, wind)
#     st.success(f"Predicted Max Temperature: {result} °C")








# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Weather Dashboard", page_icon="🌦", layout="centered")

# # ---------------- CUSTOM CSS ----------------
# st.markdown("""
# <style>
# .main {
#     background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
# }
# h1 {
#     text-align: center;
#     color: white;
#     font-size: 42px;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #ff416c, #ff4b2b);
#     color: white;
#     border-radius: 12px;
#     height: 45px;
#     width: 100%;
#     font-size: 18px;
# }
# .stSuccess {
#     background-color: #1e8449 !important;
#     color: white !important;
#     border-radius: 10px;
#     padding: 12px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- TITLE ----------------
# st.markdown("<h1>🌦 Weather Prediction Dashboard</h1>", unsafe_allow_html=True)

# # ---------------- LOAD DATA ----------------
# data = pd.read_csv("seattle-weather.csv")

# # ---------------- DATA PREVIEW ----------------
# st.subheader("📂 Dataset Preview")
# st.write(data.head())

# # ---------------- MODEL TRAINING ----------------
# X = data[['wind', 'precipitation']]
# y = data['temp_max']

# model = LinearRegression()
# model.fit(X, y)

# # ---------------- GRAPH ----------------
# st.subheader("📈 Temperature Trend")

# fig, ax = plt.subplots(figsize=(8,4))
# ax.plot(data["temp_max"], color="#00c6ff")
# ax.set_title("Maximum Temperature Over Time")
# ax.set_xlabel("Days")
# ax.set_ylabel("Temp (°C)")
# st.pyplot(fig)

# # ---------------- PREDICTION SECTION ----------------
# st.subheader("🔮 Predict Maximum Temperature")

# col1, col2 = st.columns(2)

# with col1:
#     precipitation = st.number_input("🌧 Precipitation", min_value=0.0)

# with col2:
#     wind = st.number_input("💨 Wind Speed", min_value=0.0)

# if st.button("🚀 Predict Temperature"):
#     prediction = model.predict([[wind, precipitation]])
#     result = round(prediction[0], 2)
#     st.success(f"🌡 Predicted Maximum Temperature: {result} °C")

# # ---------------- FOOTER ----------------
# st.markdown("---")
# st.caption("Built with ❤️ using Streamlit & Machine Learning")