# GPT-3 for Classification and Text Summarization
- Installation
1. Install virtualenv by running pip install virtualenv.
2. Create a new virtual environment by running virtualenv venv. 
3. Activate the virtual environment by running: 
      * `source venv/bin/activate` on Linux or macOS
      * `./venv/Scripts/activate` on Windows.
4. Install dependencies: `pip install -r requirements.txt`

- Classification use
Used for classification of sentiment 
`Datasets` will be used for fine-tuning `text-davinci-003` model 
Finetuning of GPT-3 model https://beta.openai.com/docs/guides/fine-tuning
Run application `streamlit run Classification/app.py`

- Summarization 
Used for providing summaries of texts. Will be adapted for technical report generation below
`Datasets` will be used for fine-tuning `text-davinci-003` and `text-babbage-001` models.
Finetuning of GPT-3 model https://beta.openai.com/docs/guides/fine-tuning
Run application `streamlit run Summarization/app.py`

- Report_generator 
Custom report generation


