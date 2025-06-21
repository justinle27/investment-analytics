import streamlit as st
from calculations.real_estate import cap_rate, cash_on_cash
from calculations.stocks import cagr
from utils.risk_profile import get_risk_profile

st.set_page_config(page_title="Investment Return Calculator", layout="wide")

st.title("📈 Investment Return Calculator")

option = st.sidebar.selectbox("Select Investment Type", ["Real Estate", "Stocks", "Risk Profile Quiz"])

if option == "Real Estate":
    noi = st.number_input("Net Operating Income (NOI)", value=10000.0)
    price = st.number_input("Purchase Price", value=200000.0)
    st.write("Cap Rate:", f"{cap_rate(noi, price):.2f}%")
    
    cash_flow = st.number_input("Annual Cash Flow", value=5000.0)
    investment = st.number_input("Total Cash Invested", value=40000.0)
    st.write("Cash-on-Cash Return:", f"{cash_on_cash(cash_flow, investment):.2f}%")

elif option == "Stocks":
    initial = st.number_input("Initial Investment", value=1000.0)
    final = st.number_input("Final Value", value=2000.0)
    years = st.number_input("Years Held", value=5.0)
    st.write("CAGR:", f"{cagr(initial, final, years):.2f}%")

elif option == "Risk Profile Quiz":
    st.write("Answer these 3 questions:")
    q1 = st.slider("How long will you hold your investments?", 1, 10, 5)
    q2 = st.slider("How do you handle market drops?", 1, 10, 5)
    q3 = st.slider("How important is capital preservation?", 1, 10, 5)
    total_score = q1 + q2 + q3
    st.write("Your Risk Profile:", get_risk_profile(total_score))