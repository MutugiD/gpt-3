import streamlit as st
from model_classifier import Classifier
import os 

def app():

    # Creating an object of prediction service
    pred = Classifier()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input, api_key)

    if api_key:

        # Setting up the Title
        st.title("Sentiment based on this text")

        # st.write("---")

        input = st.text_area(
            "Input your own text in English",
            #value=s_example,
            max_chars=250,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
