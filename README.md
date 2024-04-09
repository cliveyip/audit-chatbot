install requirements: langchain, streamlit
create a secrets.toml file and store your OPENAI API key there, for example OPENAI_API_KEY = sk-xxxxxxxxxxxx
store the documents you want to query under the 'pdf' folder
run "embed and load data.ipynb" to convert the pdf to text, embed them and store them in a vector database (chromadb)
in console, run 'streamlit run app.py' to run the app and view it on localhost
