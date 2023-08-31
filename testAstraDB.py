from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os, sys

username = "token"
token = os.environ['ASTRA_DB_TOKEN']
secureBundleLocation = os.environ['ASTRA_DB_SECURE_BUNDLE_LOCATION']

keyspace = sys.argv[1]
table = sys.argv[2]

cloud_config= {
        'secure_connect_bundle': secureBundleLocation,
        'use_default_tempdir': False,
}
auth_provider = PlainTextAuthProvider(username, token)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select cluster_name from system.local").one()
if row:
    print("cluster name = " + row[0])
else:
    print("An error occurred.")

pStatement = session.prepare("""
    SELECT column_name FROM system_schema.columns WHERE keyspace_name=? AND table_name=?;
""")

rows = session.execute(pStatement,[keyspace,table])
print("\nColumns for " + keyspace + "." + table)
for row in rows:
    print(row[0])
