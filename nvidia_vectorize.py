import os

from astrapy import DataAPIClient
from astrapy.constants import Environment
from astrapy.constants import VectorMetric
from astrapy.info import CollectionVectorServiceOptions

# Initialize the client and get a "Database" object
client = DataAPIClient(os.environ["HCD_TOKEN"], environment=Environment.HCD)
database = client.get_database(os.environ["HCD_API_ENDPOINT"],namespace="default_keyspace")
#print(f"* Database: {database.info().name}\n")

collection = database.create_collection(
    "nvidia_embeddings",
    metric=VectorMetric.COSINE,
    service=CollectionVectorServiceOptions(
        provider="nvidia",
        model_name="NV-Embed-QA",
    ),
)
print(f"* Collection: {collection.full_name}\n")
