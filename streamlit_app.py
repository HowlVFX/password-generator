import streamlit as st
import random
from st_copy_to_clipboard import st_copy_to_clipboard

# Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

# Title of the web app
st.title("PyPassword Generator by Swayam")

# Get user input via Streamlit form elements
nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, step=1, value=4)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, step=1, value=2)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, step=1, value=2)

# Button to generate password
if st.button("Generate Password"):
    # Create the password list with all the elements (letters, symbols, numbers)
    password = (
        random.choices(letters, k=nr_letters) +
        random.choices(symbols, k=nr_symbols) +
        random.choices(numbers, k=nr_numbers)
    )

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    # Join the list into a string
    final_password = ''.join(password)

    # Display the generated password
    st.success(f"Your generated password is: {final_password}")

    # Add "Copy to Clipboard" button
    st_copy_to_clipboard(final_password, "Copy Password to Clipboard")

# Add some additional info or instructions
st.write("Use the sliders to choose the number of letters, symbols, and numbers you'd like in your password. Then, click 'Generate Password' to get a secure, random password!")
