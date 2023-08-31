from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os, sys

username = "token"
token = os.environ['ASTRA_DB_TOKEN']
secureBundleLocation = os.environ['ASTRA_DB_SECURE_BUNDLE_LOCATION']

cloud_config= {
        'secure_connect_bundle': secureBundleLocation
}
auth_provider = PlainTextAuthProvider(username, token)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

pStatement = session.prepare("""
    SELECT * FROM sales.emp WHERE empid IN ?;
""")

employees = {99, 9559}

rows = session.execute(pStatement,[employees])
print("Employee data:\n")
for row in rows:
    print(row)
