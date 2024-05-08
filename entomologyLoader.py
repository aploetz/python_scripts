import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.vectorstores import Cassandra
from langchain.embeddings  import HuggingFaceEmbeddings

# define Astra DB vars
ASTRA_CLIENT_ID = 'token'
ASTRA_DB_KEYSPACE = "vsearch"
ASTRA_DB_TOKEN = os.environ['ASTRA_DB_APPLICATION_TOKEN']
KEYSPACE_NAME = ASTRA_DB_KEYSPACE
SECURE_CONNECT_BUNDLE_PATH = os.environ['ASTRA_SCB_PATH']
TABLE_NAME = 'langserve_rag_demo'

# connect to Astra DB
cloud_config= {
    'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_DB_TOKEN)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider, protocol_version=4)
session = cluster.connect()

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Cassandra(embeddings, session, KEYSPACE_NAME, TABLE_NAME)

# load and process file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

src_file_name = os.path.join(BASE_DIR, "sources.txt")
lines = [
    line.strip()
    for line in open(src_file_name).readlines()
    if line.strip()
    if line[0] != "#"
]

# ID == name to prevent duplicates on multiple runs
names = [
	line.split(": ")[0].lower().replace(" ", "_")
	for line in lines
	if line.split(":")[0] != "#"
]

#for line in lines:
#	print(line)

#for id in names:
#	print(id)

embeddingVectors = vectorstore.embedding.embed_documents(lines)

#for vector in embeddingVectors:
#	print(vector)

#vectorstore.add_texts(texts=lines, ids=names)

ttl_seconds = 0
batch_size: int = 16
metadatas = [{} for _ in lines]

for i in range(0, len(lines), batch_size):
    #batch_texts = lines[i : i + batch_size]
    #batch_embedding_vectors = embeddingVectors[i : i + batch_size]
    #batch_ids = names[i : i + batch_size]
    #batch_metadatas = metadatas[i : i + batch_size]

    #futures = [
    #    vectorstore.table.put_async(
    #        text, embedding_vector, text_id, metadata, ttl_seconds
    #    )
    #    for text, embedding_vector, text_id, metadata in zip(
    #        batch_texts, batch_embedding_vectors, batch_ids, batch_metadatas
    #    )
    #]
    #for future in futures:
    #    future.result()

    vectorstore.table.put(lines[i],embeddingVectors[i],names[i],metadatas[i],ttl_seconds)
