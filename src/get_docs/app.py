import streamlit as st
from docs import Docs

st.title("Get Docs")

url = st.text_input("URL")

# set three columns
col1, col2, col3 = st.columns(3)

with col3:
    max_depth = st.number_input("Max Depth", value=20)

with col2:
    sort_results = st.checkbox("Sort Results", value=True)

with col1:
    reverse_results = st.checkbox("Reverse Results", value=True)

docs = Docs(url, max_depth, sort_results, reverse_results)

if st.button("Get Docs"):
    doclist = docs.get_docs()
    for doc in doclist:
        st.markdown(f"### {doc.metadata['title']}")
        st.markdown(f"[{doc.metadata['source']}]")
        st.write(doc.page_content)
