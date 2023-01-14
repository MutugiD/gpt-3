import openai

class ReportGenerator:
    def __init__(self):
        print("Report Generator Model Intialized--->")

    def generate_report(self, input_text, myKwargs={}):
        """
        wrapper for the API to save the input text and the generated report
        """        
        # Arguments to send the API
        kwargs = {
            "engine": "text-davinci-002",
            "prompt": f"Generate a report based on the following text:\n{input_text}", 
            "temperature": 0.7, 
            "max_tokens": 2048,
            "top_p": 1.0, 
            "frequency_penalty": 0.0, 
            "presence_penalty": 0.0,
            "stop": ["."]
        }

        # update the arguments
        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]
        
        report = openai.Completion.create(**kwargs)["choices"][0]["text"].strip()
        return report
    
    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        openai.api_key = api_key
        output = self.generate_report(input)
        return output
