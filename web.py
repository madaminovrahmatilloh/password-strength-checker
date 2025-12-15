import streamlit as st
from core import check_strength_score, estimate_crack_time, COMMON_PASSWORDS

st.set_page_config(page_title="Password Strength Checker")

st.title("Password Strength Checker")

password = st.text_input("Enter a password", type="password")

if st.button("Check strength"):
    if not password:
        st.warning("Please enter a password")
    else:
        is_common = password.lower() in COMMON_PASSWORDS
        score = check_strength_score(password)
        crack_time = estimate_crack_time(password)

        if score <= 2:
            strength = "Weak password!"
        elif score == 3:
            strength = "Medium password!"
        else:
            strength = "Strong password!"

        if is_common:
            st.error("This is a very common password!")

        st.success(f"Strength: {strength}")
        st.write(f"Score: {score}")
        st.write(f"Estimated crack time: {crack_time}")
