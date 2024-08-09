from PyPDF2 import PdfReader

def extract_text_from_policy(policy_file):
    reader = PdfReader(policy_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text
