from PyPDF2 import PdfReader

def extract_text_from_policy(policy_file):
    print("extracting text")
    reader = PdfReader(policy_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    print("extracting text: done")
    return text
