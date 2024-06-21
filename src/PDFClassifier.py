from src.AIagent import AIagent
from src.PDFHandler import PDFHandler

categories = ["about", "work experience", "education", "languages", "skills", "interests"]

class PDFClassifier:
    def __init__(self, f):
        self.aiagent = AIagent("llama3")
        self.pdfhandler = PDFHandler(f)

    def classify(self, category: str) -> str:
        text = self.pdfhandler.remove_hyphens()

        prompt_category = "I want you to identify the elements of the text that are related to " + category + ". Your answer need to have this format and nothing else: { " + category + ": 'subcategory': 'description'}"

        self.aiagent.generate_response(prompt_category, False)
        return self.aiagent.generate_response(text)
    
    def classify_all(self) -> str:
        text = self.pdfhandler.remove_hyphens()

        for category in categories:
            cattxt = self.classify(category)
            with open(category + ".txt", "w") as f:
                f.write(cattxt)