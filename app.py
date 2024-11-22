import google.generativeai as genai
import os
import streamlit as st

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.environ["API_KEY"])


model = genai.GenerativeModel("gemini-1.5-flash")


# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

st.title("Write a Story")

st.write("What do you want your story to be about?")


# User input for story prompt
user_input = st.text_input("Enter your story prompt:")

# Generate story button
if st.button("Generate Story"):
    if user_input.strip():  # Check if input is not empty
        try:
            # Generate story based on user input
            response = model.generate_content(f"{user_input}")
            # Display the generated story
            st.write("Here's your story:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt to generate a story.")