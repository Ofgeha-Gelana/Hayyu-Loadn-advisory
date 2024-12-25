# import streamlit as st

# # Inject custom CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Load the CSS file
# local_css("style.css")

# # Function to check loan eligibility
# def check_eligibility(transaction_2022, transaction_2023, transaction_2024):
#     avg_transaction = (transaction_2022 + transaction_2023 + transaction_2024) / 3
#     if avg_transaction > 10000:
#         return f"Eligible for loan: {avg_transaction:.2f})"
#     else:
#         return f"Not eligible for loan"

# # Streamlit app
# st.markdown(
#     """
#     <div class="header-container">
#         <h1 class="title">Hayyu Loan Advisor</h1>
#         <p class="subtitle">Easily check loan eligibility based on transaction history</p>
        
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # Input form
# with st.form("loan_eligibility_form"):
#     st.markdown(
#         """
#         <div class="form-header">
#             <h2>Enter Customer Transaction Details</h2>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     serial_no = st.text_input("S/No", help="Enter the serial number of the customer")
#     transaction_2022 = st.number_input("2022 Transaction", min_value=0.0, help="Enter total transaction for 2022")
#     transaction_2023 = st.number_input("2023 Transaction", min_value=0.0, help="Enter total transaction for 2023")
#     transaction_2024 = st.number_input("2024 Transaction", min_value=0.0, help="Enter total transaction for 2024")
#     submit = st.form_submit_button("Check Eligibility")

# # Processing the form
# if submit:
#     if serial_no:
#         result = check_eligibility(transaction_2022, transaction_2023, transaction_2024)
#         st.markdown(
#             f"""
#             <div class="result success">
#                 <p>Result for S/No {serial_no}: <strong>{result}</strong></p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     else:
#         st.markdown(
#             """
#             <div class="result error">
#                 <p>Please enter a valid serial number!</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )


import streamlit as st

# Inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
local_css("style.css")

# Function to check loan eligibility
def check_eligibility(transaction_2022, transaction_2023, transaction_2024):
    avg_transaction = (transaction_2022 + transaction_2023 + transaction_2024) / 3
    if avg_transaction > 10000:
        return f"Eligible for loan: {avg_transaction:.2f}", "success"
    else:
        return f"Not eligible for loan", "error"

# Streamlit app
st.markdown(
    """
    <div class="header-container">
        <h1 class="title">Hayyu Loan Advisor</h1>
        <p class="subtitle">Easily check loan eligibility based on transaction history</p>
        
    </div>
    """,
    unsafe_allow_html=True,
)

# Input form
with st.form("loan_eligibility_form"):
    st.markdown(
        """
        <div class="form-header">
            <h2>Enter Customer Transaction Details</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    serial_no = st.text_input("S/No", help="Enter the serial number of the customer")
    transaction_2022 = st.number_input("2022 Transaction", min_value=0.0, help="Enter total transaction for 2022")
    transaction_2023 = st.number_input("2023 Transaction", min_value=0.0, help="Enter total transaction for 2023")
    transaction_2024 = st.number_input("2024 Transaction", min_value=0.0, help="Enter total transaction for 2024")
    submit = st.form_submit_button("Check Eligibility")

# Processing the form
if submit:
    if serial_no:
        result, result_class = check_eligibility(transaction_2022, transaction_2023, transaction_2024)
        st.markdown(
            f"""
            <div class="result {result_class}">
                <p>Result for S/No {serial_no}: <strong>{result}</strong></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result error">
                <p>Please enter a valid serial number!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
