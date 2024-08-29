import os

from astrapy import DataAPIClient
from astrapy.constants import Environment

# connection
DB_APPLICATION_TOKEN = os.environ.get("DB_APPLICATION_TOKEN")
DB_API_ENDPOINT= os.environ.get("DB_API_ENDPOINT")

client = DataAPIClient(DB_APPLICATION_TOKEN, environment=Environment.OTHER)
db = client.get_database(DB_API_ENDPOINT)

collections = db.list_collections()
for coll_desc in collections:
    print(coll_desc)
