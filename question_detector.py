import nltk
from nltk.tokenize import sent_tokenize

# ✅ Ensure only "punkt" is downloaded (not "punkt_tab")
nltk.download("punkt")

def detect_questions(text):
    sentences = sent_tokenize(text)
    questions = [sent for sent in sentences if "?" in sent]
    return questions

# ✅ Test function
if __name__ == "__main__":
    sample_text = "What is AI? AI stands for Artificial Intelligence. How does it work? It learns from data."
    questions_found = detect_questions(sample_text)
    print("Detected Questions:", questions_found)
