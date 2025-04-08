from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def build_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks, embeddings)
