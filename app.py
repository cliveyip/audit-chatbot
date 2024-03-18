from langchain.llms import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

import streamlit as st

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(persist_directory="chroma_db", embedding_function=embedding_function)

llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

st.title('Audit Chatbot 🤖')

def generate_response(input_text, source_selected):
    
    search_kwargs = {}

    if source_selected == 'All sources':
        search_kwargs = {}
    elif source_selected == 'IIA Implementation-Guides.pdf':
        search_kwargs = {"filter":{"source":"./pdf/IIA Implementation-Guides.pdf"}}
    elif source_selected == 'IIA Standards - Audit Manual.pdf':
        search_kwargs = {"filter":{"source":"./pdf/IIA Standards - Audit Manual.pdf"}}

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs=search_kwargs)
        # retriever=db.as_retriever(search_kwargs={"filter":{"source":"./pdf/IIA Implementation-Guides.pdf"}})
    )

    st.info(qa.invoke(input_text)['result'])

with st.form('my_form'):
    text = st.text_area('Enter text:', placeholder="What would you like to know about auditing?")
    option = st.selectbox(
    'Select source document:',
    ('All sources', 'IIA Implementation-Guides.pdf', 'IIA Standards - Audit Manual.pdf'))
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text, option)

