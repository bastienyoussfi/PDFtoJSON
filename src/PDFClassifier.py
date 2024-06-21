from AIagent import AIagent
from PDFHandler import PDFHandler

class PDFClassifier:
    def __init__(self, f):
        self.aiagent = AIagent("llama3")
        self.pdfhandler = PDFHandler(f)

    def classify(self, category: str) -> str:
        text = self.pdfhandler.remove_hyphens()

        prompt_category = "I want you to identify the elements of the text that are related to " + category + ". Send the results to me in a list and don't include any other information."

        self.aiagent.generate_response(prompt_category)
        return self.aiagent.generate_response(text)