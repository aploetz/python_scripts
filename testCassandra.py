from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

# initializing variable defaults
hostname="127.0.0.1"
username="cassandra"
password="cassandra"

#check arguments for overrides
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]

nodes = []
nodes.append(hostname)

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth_provider)
session = cluster.connect()

rows = session.execute("SELECT key FROM system.local;")
for row in rows:
    print(row[0])
