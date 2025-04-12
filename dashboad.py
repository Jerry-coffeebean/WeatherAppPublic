# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib as plt

# Function to load example data (replace with your actual data source)
def load_data():
    # Create a sample DataFrame with actual and predicted temperature data
    data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=7, freq='D'),
        'Actual Temperature (°C)': [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
],
        'Predicted Temperature (°C)': [-49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, -37, -36, -35, -34, -33, -32, -31, -30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50
]
    })
    return data

# Load the sample data

dataread = pd.read_csv('C:/Users/Manodeepa/Downloads/cleaned_weather_data.csv')

# Streamlit application layout
st.title("Weather Dashboard")  # App title
st.header("Your Weather Insights")  # App header

# Display the data in a table format
st.subheader("Temperature Data")
st.write("Below is the actual and predicted temperature data for the week:")
print(type(dataread))
st.dataframe(dataread)

# Display actual temperature as a metric
actual_avg_temp = data["Actual Temperature (°C)"].mean()
st.subheader("Metrics")
st.metric(label="Average Actual Temperature (°C)", value=round(actual_avg_temp, 2))

# Display predicted temperature as a metric
predicted_avg_temp = data["Predicted Temperature (°C)"].mean()
st.metric(label="Average Predicted Temperature (°C)", value=round(predicted_avg_temp, 2))

# Plot a graph for Actual vs Predicted temperature
st.subheader("Actual vs Predicted Temperature Trend")
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Actual Temperature (°C)'], label='Actual Temperature', marker='o')
plt.plot(data['Date'], data['Predicted Temperature (°C)'], label='Predicted Temperature', marker='o')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Actual vs Predicted Temperature')
plt.legend()
plt.grid()
st.pyplot(plt)  # Display the plot using Streamlit

# Footer message
st.write("Weather Dashboard App for Hackathon 2025")