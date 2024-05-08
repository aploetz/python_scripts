import os

from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymongo import MongoClient

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

loader = PyPDFLoader("https://arxiv.org/pdf/2303.08774.pdf")
data = loader.load()
docs = text_splitter.split_documents(data)

DB_NAME = "langchain_db"
COLLECTION_NAME = "atlas_collection"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"
MONGODB_ATLAS_CLUSTER_URI = uri = os.environ.get("MONGO_DB_ENDPOINT")

client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

vector_search = MongoDBAtlasVectorSearch.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(disallowed_special=()),
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)

query = "What were the compute requirements for training GPT 4"
results = vector_search.similarity_search(query)
print("result: ", results)