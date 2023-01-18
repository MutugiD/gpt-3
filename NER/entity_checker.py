import openai
import streamlit as st

# st.secrets["pass"] is accessing the value of the "pass" secret.
openai.api_key = st.secrets["api"]

st.header("ER Creator")
# Create Text Area Widget to enable user to enter texts
text = st.text_area("Enter instructions here")
#st.file_uploader("Upload files")

if len(text) > 100: 
    temp = st.slider("temperature", 0.0, 1.0, 0.5)
    if st.button("Generate"): 
        response = openai.Completion.create(
                    engine = "text-davinci-003",
                    prompt= 'Find the snippet of text containing the [LEGAL TERM] from the following statement in a legal contract: [STATEMENT FROM A CONTRACT]' + text, 
                    #Start the demand letter by stating - We act for [ ] Limited (hereinafter "our Client") and have instructions to address you as hereunder:' + text,
                    max_tokens = 512,
                    temperature = temp)
        res = response["choices"][0]["text"] 
        st.info(res)
        st.download_button("Download", res)
else: 
    st.warning("Instructions issued are not sufficient")
    
