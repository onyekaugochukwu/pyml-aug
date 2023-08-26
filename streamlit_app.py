import streamlit as st
import sklearn
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Week 2: The Airbnb dataset of Amsterdam")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)

price_in_dollars = st.number_input('Enter the USD price of the listed apartment')
amenities = st.slider('How many amenities does the listing have?', 0, 50, 20)


user_input = [[price_in_dollars, amenities]]

if st.button('Predict?'):
    st.write("The model predicts that the average tip for this listing is:", model.predict(user_input).round(2))
