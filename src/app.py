from src.scraper import scrape_page
from src.loader import split_text
from src.embedder import build_vectorstore
from src.qa_agent import create_agent

def main():
    url = input("Enter doc URL: ")
    raw = scrape_page(url)
    chunks = split_text(raw)
    db = build_vectorstore(chunks)
    agent = create_agent(db)

    while True:
        q = input("Ask a question (or 'exit'): ")
        if q == 'exit': break
        print(agent.run(q))

if __name__ == "__main__":
    main()
