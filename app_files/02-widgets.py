# Using widgets we can create more interactive applications
# Streamlit provides amazing widgets

import streamlit as st
import pandas as pd

st.title("Streamlit taking input")


## take the name
name = st.text_input("Enter you name: ")
if name:  # if name is not None, meaning that if the user puts in some text.
    st.write(f"Hello {name}, Welcome")



## use a slider to take the age
# min=0, max=50, the fourth parameter which we didn't specify would be the default value of the slider when loaded.
age = st.slider("Select your age please ", 0, 50) 

if age:
    st.write(f"you are {age} years old")
    if age<10:
        st.write("you are not allowed to use this app")
    elif 10<=age<=30:
        st.write("your age is between 10 and 30. very good")
    else:
        st.write("your age is between 31 and 50. thank you")


## Select box (like drop-down box)
options = ["Python", "Java", "Julia", "C#", "C++"]
choice = st.selectbox("Select your favourite programming laguage: ", options)
st.write(f"you selected {choice}")


## DataFrame
data = {
    "name":["Ehsan", "Jake", "John", "Bob"],
    "age":[30, 35, 24, 41],
    "city":["Sanandaj", "London", "Chicago", "Houston"]
}

df = pd.DataFrame(data=data)
st.write(df)


## Upload botton
uploaded_file = st.file_uploader("Choose a csv file to upload", type='csv') # for the type parameter, you can give a list.

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)