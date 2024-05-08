import os

from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

loader = PyPDFLoader("https://arxiv.org/pdf/2303.08774.pdf")
data = loader.load()
docs = text_splitter.split_documents(data)
atlas_collection = "atlas_collection"

ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")

vector_search = AstraDBVectorStore.from_documents(
  documents=docs,
  embedding=OpenAIEmbeddings(disallowed_special=()),
  collection_name=atlas_collection,
  api_endpoint=ASTRA_DB_API_ENDPOINT,
  token=ASTRA_DB_APPLICATION_TOKEN,
)

query = "What were the compute requirements for training GPT 4"
results = vector_search.similarity_search(query)
print("result: ", results)