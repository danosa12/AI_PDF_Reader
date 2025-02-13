from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

# Fix: Download the required NLTK data before using it
nltk.download("punkt")

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Test Function
if __name__ == "__main__":
    sample_text = "Artificial Intelligence is a broad field of computer science. It aims to build intelligent machines. AI systems can solve complex problems, learn from data, and make decisions."
    summary = summarize_text(sample_text)
    print("Summary:", summary)
