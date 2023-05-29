from pdfquery import PDFQuery
import os
raw_folder = "../../raw_data/deep_afppred/"

for filename in os.listdir(raw_folder):
    print(filename)
    pdf = PDFQuery(raw_folder + filename)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_elements]

    print(text)
