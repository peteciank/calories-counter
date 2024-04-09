# Import necessary libraries
import streamlit as st  # Import Streamlit library for creating web application

# Define exercise options and corresponding calories burned per hour
exercise_options = {
    "Running 🏃‍♂️": 600,
    "Cycling 🚴‍♀️": 500,
    "Swimming 🏊‍♂️": 700,
    "Walking 🚶‍♂️": 300,
    "Jumping Rope 🏋️‍♀️": 800
}

# Define function to calculate calories burned based on exercise and duration
def calculate_calories(exercise, duration):
    calories_per_hour = exercise_options[exercise]
    calories_burned = calories_per_hour * duration / 60  # Calculate calories burned for given duration
    return calories_burned

# Set page title and icon
st.set_page_config(page_title='Calories Burned Calculator', page_icon='🔥')

# Display title and description
st.title('Calories Burned Calculator 🏋️‍♂️')
st.write("Calculate the approximate number of calories burned during exercise based on duration.")

# Select exercise and display calories burned per hour
selected_exercise = st.selectbox("Select an exercise", list(exercise_options.keys()))
calories_per_hour = exercise_options[selected_exercise]
st.write(f"Calories burned per hour for {selected_exercise}: {calories_per_hour} kcal")

# Select exercise duration
duration = st.slider("Select exercise duration (minutes)", 0, 120, 30)

# Calculate and display approximate calories burned
calories_burned = calculate_calories(selected_exercise, duration)
st.write(f"Approximate calories burned for {duration} minutes of {selected_exercise}: {calories_burned:.2f} kcal")

# Display badge
st.markdown("""
    <div style="display: flex; align-items: center;">
        <img src="https://raw.githubusercontent.com/peteciank/public_files/main/mugshot_light.png" alt="Profile Picture" style="border-radius: 50%; margin-right: 20px;width: 50px; height: 50px;">
        <div>
            <p style="font-weight: bold; margin-bottom: 5px;">Created by Pete Ciank</p>
            <p style="margin: 0;">Streamlit enthusiast, Tech Lover, Product and Project Manager 💪</p>
        </div>
    </div>
""", unsafe_allow_html=True)

with st.expander("📃 Download Resume / Cover", expanded=False):
    st.markdown('📖 My [LinkedIn](https://www.linkedin.com/in/pedrociancaglini/) Profile.')
    st.markdown('🌎 My [Website](https://sites.google.com/view/pedrociancaglini)')
    st.markdown('👩‍💻 My [Github](https://github.com/peteciank/)')
    st.markdown('🔽 [Download](https://github.com/peteciank/public_files/blob/main/Ciancaglini_Pedro_Resume_v24.pdf) my Resume')
    st.markdown('🔽 [Download](https://github.com/peteciank/public_files/blob/main/Cover%20Letter.pdf) my Letter')
