import streamlit as st
from datetime import datetime


st.markdown("""
<style>
/* All your CSS here */
</style>

<!-- Your HTML & JS here -->

""", unsafe_allow_html=True)


st.set_page_config(page_icon="🧮",page_title="AGE CALCULATOR")
st.title("🎂 Age calculator")
st.write("Enter your Birth date below(date/month/year) format:")
dob = st.text_input("Enter your Birth date (dd/mm/yyyy): ")

now = datetime.now()
f_day = now.day
f_month = now.month
f_year = now.year

if st.button("Calculate Age"):
    try:
        r_day,r_month,r_year = map(int,dob.split("/"))

        years =f_year - r_year
        months =f_month - r_month
        days =f_day - r_day

        if days<0:
            months-=1
            days+=30
        if months<0:
            years-=1
            months+=12

        st.success(f"Your Age is: {years} years ,{months} months and {days} days")

    except ValueError:
        st.error("❌ Invalid input ! Please enter in valid format (dd/mm/yyyy)")
