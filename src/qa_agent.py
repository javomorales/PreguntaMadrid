from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def create_agent(vectorstore):
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(), retriever=vectorstore.as_retriever()
    )
