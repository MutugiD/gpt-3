
- Installation
1. Create a new virtual environment by running `virtualenv venv`. 
2. Activate the virtual environment by running: 
      * `source venv/bin/activate` on Linux or macOS
      * `./venv/Scripts/activate` on Windows.
3. Install dependencies: `pip install -r requirements.txt`

- Classification use
1. Used for classification of sentiment 
2. Run application `streamlit run Classification/app.py`

- Summarization 
1. Used for providing summaries of texts. For this sample, it is used for generating a downloadable report from demand letter instructions issued by a legal officer of a credit union.
2. Run application `streamlit run Summarization/summarizer.py`
3. Could be adopted for various custom uses (WIP)

- Report_generator 
1. Custom report generation
2. Run application `streamlit run Report_generator/demand_letter_generator.py`
3. Paste the text from `instructions.txt`

- Fine-tuning 
1. Synthetic data will be used for fine-tuning  
   `python Finetuning/sync_finetune_data.py` for synching the pairs in prompts and completions   
   `python Finetuning/finetune.py` for basic finetuning i.e. without hyperparameters   
2. Finetuning for cost, latency, epochs, and model performance - `python optimizer.py`  
3. Approaches:   
   a. Generic https://beta.openai.com/docs/guides/fine-tuning  
   b. Embedding https://beta.openai.com/docs/guides/embeddings/what-are-embeddings  
