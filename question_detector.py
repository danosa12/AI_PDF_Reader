import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def detect_questions(text):
    doc = nlp(text)
    questions = [sent.text for sent in doc.sents if "?" in sent.text]
    return questions

# Test Function
if __name__ == "__main__":
    sample_text = "What is AI? AI stands for Artificial Intelligence. How does it work? It learns from data."
    questions_found = detect_questions(sample_text)
    print("Detected Questions:", questions_found)
