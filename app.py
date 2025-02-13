import streamlit as st
from pdf_extractor import extract_text_from_pdf
from question_detector import detect_questions
from summarizer import summarize_text
from main import ask_chatgpt

st.title("📄 AI PDF Reader")

# Upload PDF File
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.write("Extracted Text:")
    st.text_area("PDF Content", pdf_text, height=200)

    # Summarize PDF
    if st.button("Summarize PDF"):
        summary = summarize_text(pdf_text, num_sentences=3)
        st.write("**Summary:**", summary)

    # Detect Questions in PDF
    questions = detect_questions(pdf_text)
    if questions:
        st.write("Detected Questions:")
        for q in questions:
            st.write(f"- {q}")
    else:
        st.write("No questions detected.")

    # Ask a Question
    question = st.text_input("Ask a Question:")
    
    if st.button("Get Answer"):
        if question.strip():
            answer = ask_chatgpt(question, pdf_text)
            st.write("**Answer:**", answer)
        else:
            st.warning("Please enter a question.")
