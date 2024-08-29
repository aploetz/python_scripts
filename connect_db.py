from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from os import path, environ

import json

#with open(ASTRA_TOKEN_PATH, "r") as f:
#    creds = json.load(f)
#    ASTRA_DB_APPLICATION_TOKEN = creds["token"]

ASTRA_DB_APPLICATION_TOKEN = environ.get("ASTRA_TOKEN")
ASTRA_DB_SECURE_BUNDLE_PATH = environ.get("ASTRA_SCB")

cluster = Cluster(
    cloud={
        "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH,
    },
    auth_provider=PlainTextAuthProvider(
        "token",
        ASTRA_DB_APPLICATION_TOKEN,
    ),
)

session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")