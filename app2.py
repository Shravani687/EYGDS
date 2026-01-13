import streamlit as st

st.title("Some basic commands like sliders,buttons etc")

age = st.slider("Enter your age",1,100)
city = st.selectbox("Select your city",["delhi","Pune","banglore","chennai"])

if st.button("submit"):
    st.write(f"Your age is {age} and you live in {city}")