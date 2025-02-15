import nltk
from nltk.tokenize import sent_tokenize

# Download required tokenizer (Fixes LookupError)
nltk.download("punkt")
print("✅ NLTK punkt tokenizer is installed and ready to use!")

def detect_questions(text):
    sentences = sent_tokenize(text)
    questions = [sent for sent in sentences if "?" in sent]
    return questions

# Test Function
if __name__ == "__main__":
    sample_text = "What is AI? AI stands for Artificial Intelligence. How does it work? It learns from data."
    questions_found = detect_questions(sample_text)
    print("Detected Questions:", questions_found)
