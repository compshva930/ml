import streamlit as st
import pandas as pd

# 1. App Title and Markdown Text
st.title("My First Streamlit App")
st.write("Welcome to your new dashboard! Streamlit lets you build web apps with simple Python scripts.")

# 2. Interactive Input Widgets
st.header("User Input Section")

# Text Input
user_name = st.text_input("Enter your name:", "Guest")

# Slider Input
age = st.slider("Select your age:", min_value=0, max_value=100, value=25)

# Dropdown Selection
favorite_color = st.selectbox(
    "What is your favorite color?",
    options=["Blue", "Green", "Red", "Yellow"]
)

# 3. Dynamic Output Base on Inputs
st.subheader("Your Profile Summary")
st.write(f"Hello **{user_name}**!")
st.write(f"You are **{age}** years old and your favorite color is **{favorite_color}**.")

# 4. Displaying Data and Charts
st.header("Data and Visualization")

# Toggle to show/hide data
if st.checkbox("Show sample chart data"):
    # Create a simple DataFrame
    chart_data = pd.DataFrame(
        {
            "Day 1": [10, 20, 15, 30],
            "Day 2": [20, 30, 25, 40]
        }
    )
    
    # Display the interactive dataframe table
    st.dataframe(chart_data)
    
    # Render an interactive line chart
    st.line_chart(chart_data)
