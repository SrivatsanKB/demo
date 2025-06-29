import streamlit as st 
from demopython import area_of_circle

st.title("My app for area of Circle")


page=st.sidebar.selectbox("Slect a page",["Home","Area calculator"])
if page=="Home":
    st.write("This app is made to calculate area of circle which is useful for students as well as professionals who want to quickly know area of circle")
elif page== "Area calculator":
    a=st.number_input("Enter the radius")
    st.write("Area of Circle",area_of_circle(a))
st.write("Thank You for choosing our app")
