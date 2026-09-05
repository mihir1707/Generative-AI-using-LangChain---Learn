from langchain_core.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)