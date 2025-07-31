import streamlit as st
import openai

st.set_page_config(page_title="Flight Booking Chatbot")

st.title("✈️ Flight Booking Chatbot Assistant")

openai.api_key = st.secrets["openai_api_key"]

flights = [
    {"id": "EK201", "from": "Dubai", "to": "London", "date": "2025-08-10", "price": "AED 2500"},
    {"id": "QR310", "from": "Dubai", "to": "London", "date": "2025-08-10", "price": "AED 2200"},
    {"id": "BA114", "from": "Dubai", "to": "London", "date": "2025-08-10", "price": "AED 2300"}
]

def find_flights(from_city, to_city, date):
    return [f for f in flights if f["from"] == from_city and f["to"] == to_city and f["date"] == date]

st.sidebar.header("Enter Flight Details")
from_city = st.sidebar.text_input("From", "Dubai")
to_city = st.sidebar.text_input("To", "London")
travel_date = st.sidebar.date_input("Travel Date")

if st.sidebar.button("Search Flights"):
    results = find_flights(from_city, to_city, str(travel_date))
    if results:
        st.success("Flights found:")
        for f in results:
            st.write(f"- {f['id']} | {f['from']} → {f['to']} | {f['date']} | {f['price']}")
    else:
        st.warning("No flights found for the selected route and date.")

user_input = st.text_input("Ask the AI assistant anything related to flights:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a flight booking assistant. Help the user find and book flights."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write("✈️ Assistant:", response['choices'][0]['message']['content'])
