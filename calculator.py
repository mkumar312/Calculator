import streamlit as st

# ---------------- PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND) ----------------
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>🧮 Simple Streamlit Calculator</h1>", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
st.write("### Enter two numbers:")

num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# ---------------- OPERATION SELECT ----------------
st.write("### Select Operation:")
operation = st.selectbox(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# ---------------- CALCULATE ----------------
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"✔ Result: {result}")

    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"✔ Result: {result}")

    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"✔ Result: {result}")

    elif operation == "Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"✔ Result: {result}")
