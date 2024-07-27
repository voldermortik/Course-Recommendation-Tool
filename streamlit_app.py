import streamlit as st
import streamlit.components.v1 as components

# Function to read HTML file
def load_html(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Load HTML content
html_string = load_html('course_selection.html')  
# Replace 'index.html' with the path to your HTML file

# Embed HTML content in Streamlit app
components.html(html_string, height=800, scrolling=True)
