import streamlit as st
import streamlit.components.v1 as components

# Function to read HTML file
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Load HTML content
html_string = load_html('course_selection.html')  
# Replace 'course_selection.html' with the path to your HTML file

# Embed HTML content in Streamlit app with dynamic height
components.html(html_string, height=1000, width=1200, scrolling=False)
