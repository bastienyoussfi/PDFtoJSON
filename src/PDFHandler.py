from pypdf import PdfReader
from typing import List

PATH = "./data/"

# Removes hyphens from a line
def dehyphenate(lines: List[str], line_no: int) -> List[str]:
    next_line = lines[line_no + 1]
    word_suffix = next_line.split(" ")[0]

    lines[line_no] = lines[line_no][:-1] + word_suffix
    lines[line_no + 1] = lines[line_no + 1][len(word_suffix) :]
    return lines

# PDF Handler for a one page PDF
class PDFHandler:
    def __init__(self, f):
        self.reader = PdfReader(PATH + f)
        self.page = self.reader.pages[0]
        self.text = self.page.extract_text(0)

    # Remove hypens from the PDF for better processing
    def remove_hyphens(self) -> str:
        lines = [line.rstrip() for line in self.text.split("\n")]

        # Find dashes
        line_numbers = []
        for line_no, line in enumerate(lines[:-1]):
            if line.endswith("-"):
                line_numbers.append(line_no)

        # Replace
        for line_no in line_numbers:
            lines = dehyphenate(lines, line_no)

        return "\n".join(lines)
    
    def save_pdf(self, output: str):
        with open(output, "w") as f:
            f.write(self.remove_hyphens())    