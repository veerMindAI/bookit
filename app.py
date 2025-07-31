import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Flight Booking Chatbot Assistant")
st.title("✈️ Flight Booking Chatbot")

# ✅ NEW WAY: use OpenAI client
client = OpenAI(api_key=st.secrets["openai_api_key"])

flights = [
    {"id": "EK201", "from": "Dubai", "to": "London", "date": "2025-08-10", "price": "AED 2500"},
    {"id": "QR310", "from": "Dubai", "to": "London", "date": "2025-08-10", "price": "AED 2200"},
    {"id": "BA114", "from": "Dubai", "to": "London", "date": "2025-08-10", "price": "AED 2300"}
]

st.sidebar.header("Enter Flight Details")
from_city = st.sidebar.text_input("From", "Dubai")
to_city = st.sidebar.text_input("To", "London")
travel_date = st.sidebar.date_input("Travel Date")

def find_flights(from_city, to_city, date):
    return [f for f in flights if f["from"] == from_city and f["to"] == to_city and f["date"] == date]

if st.sidebar.button("Search Flights"):
    results = find_flights(from_city, to_city, str(travel_date))
    if results:
        st.success("Flights found:")
        for f in results:
            st.write(f"- {f['id']} | {f['from']} → {f['to']} | {f['date']} | {f['price']}")
    else:
        st.warning("No flights found.")

user_input = st.text_input("Ask the AI assistant anything related to flights:")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful flight booking assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("✈️ Assistant:", response.choices[0].message.content)
