# GPT-3 for Classification and Text Summarization
- Installation
1. Install virtualenv by running `pip install virtualenv`.
2. Create a new virtual environment by running virtualenv venv. 
3. Activate the virtual environment by running: 
      * `source venv/bin/activate` on Linux or macOS
      * `./venv/Scripts/activate` on Windows.
4. Install dependencies: `pip install -r requirements.txt`

- Classification use
1. Used for classification of sentiment 
2. `Datasets` will be used for fine-tuning `text-davinci-003` model
3. Finetuning of GPT-3 model https://beta.openai.com/docs/guides/fine-tuning
4. Run application `streamlit run Classification/app.py`

- Summarization 
1. Used for providing summaries of texts. Will be adapted for technical report generation below
2. `Datasets` will be used for fine-tuning `text-davinci-003` and `text-babbage-001` models.
3. Finetuning of GPT-3 model https://beta.openai.com/docs/guides/fine-tuning
4. Run application `streamlit run Summarization/app.py`

- Report_generator 
1. Custom report generation


