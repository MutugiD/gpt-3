# GPT-3 for Classification and Text Summarization
- Installation
1. Create a new virtual environment by running `virtualenv venv`. 
2. Activate the virtual environment by running: 
      * `source venv/bin/activate` on Linux or macOS
      * `./venv/Scripts/activate` on Windows.
3. Install dependencies: `pip install -r requirements.txt`

- Classification use
1. Used for classification of sentiment 
2. `Datasets` will be used for fine-tuning `ada` and `text-davinci-003` model
3. Finetuning of GPT-3 model https://beta.openai.com/docs/guides/fine-tuning
4. Run application `streamlit run Classification/app.py`

- Summarization 
1. Used for providing summaries of texts. For this sample, it is used for generating a downloadable report from demand letter instructions issued by a legal officer of a credit union.
2. `Datasets` will be used for fine-tuning various models models.
3. Finetuning of GPT-3 model https://beta.openai.com/docs/guides/fine-tuning
4. Run application `streamlit run Summarization/summarizer.py`
5. Could be adopted for various custom uses (WIP)

- Report_generator 
1. Custom report generation
2. Run application `streamlit run Report_generator/demand_letter_generator.py`
3. Paste the text from `instructions.txt`
4. Building a custom upload link 
5. Could be adopted for various custom uses (WIP)


