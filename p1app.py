import streamlit as st
import pandas as pd

# Title
st.title("Growth Mindset Challenge")
st.write("This survey collects feedback on learning experiences to boost a growth mindset.")

# Survey Form
name = st.text_input("Your Name")
experience = st.selectbox("How was your learning experience?", ["Excellent", "Good", "Average", "Needs Improvement"])
challenges = st.text_area("What challenges did you face?")
improvements = st.text_area("Any suggestions to improve the internship program?")

# Likert Scale Questions
questions = [
    "I believe I can improve my skills with effort.",
    "I see challenges as opportunities to grow.",
    "I learn from my mistakes and failures.",
    "I seek feedback to improve my skills.",
    "I stay motivated even when tasks are difficult."
]

# Collect responses
responses = []
st.subheader("Answer the following questions:")
for question in questions:
    response = st.radio(question, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])
    responses.append(response)

# Store responses in a CSV file
FILE_NAME = "growth_mindset_responses.csv"

def save_response(name, experience, challenges, improvements, responses):
    df = pd.DataFrame([[name, experience, challenges, improvements] + responses], 
                      columns=["Name", "Experience", "Challenges", "Suggestions"] + [f"Q{i+1}" for i in range(len(questions))])
    try:
        existing_data = pd.read_csv(FILE_NAME)
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv(FILE_NAME, index=False)

if st.button("Submit Feedback"):
    if name and experience and challenges and improvements and all(responses):
        save_response(name, experience, challenges, improvements, responses)
        st.success("Thank you for your feedback!")
    else:
        st.warning("Please fill all fields before submitting.")

# View Responses
if st.checkbox("Show All Responses"):
    try:
        responses = pd.read_csv(FILE_NAME)
        st.dataframe(responses)
    except FileNotFoundError:
        st.write("No responses yet.")