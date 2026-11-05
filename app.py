import streamlit as st
from analyzer import DocumentAnalyzer

st.set_page_config(page_title="GenAI Document Analyzer", page_icon="🤖", layout="wide")

st.title("🤖 Generative AI Document Analyzer")
st.markdown("Upload any document (reports, papers, datasets) to generate intelligent executive summaries and ask questions in real-time.")

uploaded_file = st.file_uploader("Upload Text Document (.txt, .md)", type=["txt", "md"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8", errors="ignore")
    st.success(f"Loaded: {uploaded_file.name} ({len(text.split())} words)")
    
    analyzer = DocumentAnalyzer()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📄 Document Summary")
        summary = analyzer.generate_summary(text)
        st.info(summary)
        
    with col2:
        st.subheader("💡 Key Takeaways")
        points = analyzer.extract_key_points(text)
        for p in points:
            st.markdown(f"- {p}")
            
    st.divider()
    st.subheader("💬 Ask Questions About the Document")
    user_q = st.text_input("Enter your question:")
    if user_q:
        answer = analyzer.answer_question(text, user_q)
        st.write("**Answer:**", answer)
