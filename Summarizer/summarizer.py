import openai
import streamlit as st

# st.secrets["pass"] is accessing the value of the "pass" secret.
openai.api_key = st.secrets["api"]

# Create Text Area Widget to enable user to enter texts
st.header("Summarizer created by OpenAI and Streamlit")

text = st.text_area("Enter your text to summarize here")
#st.file_uploader("Upload files")
if len(text) > 100: 
    temp = st.slider("temperature", 0.0, 1.0, 0.5)
    if st.button("Generate Summary"): 
        response = openai.Completion.create(
                    engine = "text-davinci-003",
                    prompt = "Summarize the legal instructions issued, communication details to and from, including all dates the client was reached via communication means, events in between these dates, any sums of money transacted/to be transacted (on different between the dates), description of tangible/intangible assets in questions, while maintaining legal jargon." + text,
                    max_tokens = 512,
                    temperature = temp)
        res = response["choices"][0]["text"] 
        st.info(res)
        st.download_button("Download", res)
else: 
    st.warning("Text inputted too short")