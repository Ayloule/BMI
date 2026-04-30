import streamlit as st
st.title("Welcome to BMI Calculator")

#Weight input
weight = st.number_input("Enter your weight (in kgs) :")

#Height format selection
height_format = st.radio("Select your height format:", ("cms", "meters", "feet"))

#Height input
height = st.number_input("Enter your height")


#Convert height to meters
if height_format == "cms":
                         height_m = height /100
elif height_format == "feet":
    height_m = height /3.28
else :
    height_m = height

#Calculate BMI button
if st.button("Calculate BMI"):
    
    #BMI calculation
    bmi = weight /(height_m ** 2) 

    #Display BMI
    st.write(f"Your BMI index is {bmi}")

    #Determine category
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif (bmi > 16) and (bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi > 18.5) and (bmi < 25):
        st.success("Healthy")
    elif (bmi > 25) and (bmi < 30) :
        st.warning("Overweight")
    else :
        st.error("You are Extremely Overweight")
