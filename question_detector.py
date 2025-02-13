import nltk
from nltk.tokenize import sent_tokenize

# Download necessary NLP model (only needed once)
nltk.download("punkt")

def detect_questions(text):
    sentences = sent_tokenize(text)
    questions = [sent for sent in sentences if "?" in sent]
    return questions
