from flask import Flask, request, jsonify, render_template
import pdfplumber
import nltk
from nltk.tokenize import sent_tokenize
import openai
import os

# Ensure required NLTK package is downloaded
nltk.download("punkt")

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

# Function to detect questions
def detect_questions(text):
    sentences = sent_tokenize(text)
    questions = [sent for sent in sentences if "?" in sent]
    return questions

# Function to get answers using OpenAI API
def ask_openai(question, context):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure API key is set
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI assistant."},
                  {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}]
    )
    return response["choices"][0]["message"]["content"]

# Home Route
@app.route("/")
def home():
    return render_template("index.html")  # Create a frontend later

# Upload PDF Route
@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "pdf" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf_file = request.files["pdf"]
    text = extract_text_from_pdf(pdf_file)
    questions = detect_questions(text)

    return jsonify({"extracted_text": text, "detected_questions": questions})

# Ask Question Route
@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question")
    context = data.get("context")

    if not question or not context:
        return jsonify({"error": "Missing question or context"}), 400

    answer = ask_openai(question, context)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
