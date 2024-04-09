1. install requirements: langchain, streamlit
2. add a file called secrets.toml in a folder called .streamlit at the root of your app repo, and save your OPENAI API key there, for example OPENAI_API_KEY = sk-xxxxxxxxxxxx
3. store the documents you want to query under the 'pdf' folder
4. run "embed and load data.ipynb" to convert the pdf to text, embed them and store them in a vector database (chromadb)
5. use the command 'streamlit run app.py' to run the app and view it on localhost
