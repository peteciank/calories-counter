import streamlit as st  # Import Streamlit library for creating web application

# Set page title
st.title('Exercise Calorie Burn Calculator')

# Create a sidebar for input
with st.sidebar:
    st.header('Exercise Details')  # Sidebar header for exercise details
    exercise_name = st.text_input('Exercise Name', 'Running')  # Text input widget for exercise name
    duration_minutes = st.number_input('Duration (minutes)', min_value=1, max_value=120, value=30)  # Number input widget for exercise duration

# Calculate calorie burn
calories_burned_per_minute = 10  # Assume 10 calories burned per minute (adjust as needed)
total_calories_burned = calories_burned_per_minute * duration_minutes  # Calculate total calories burned

# Display result
st.subheader('Calories Burned:')  # Subheader for result
st.write(f'You burned approximately {total_calories_burned} calories by {duration_minutes} minutes of {exercise_name.lower()}.')  # Display calculated calories burned
