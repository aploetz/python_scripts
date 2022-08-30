from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

# initializing variable defaults
hostname="127.0.0.1"
username="cassandra"
password="cassandra"
protocol=4

#check arguments for overrides
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]

nodes = []
nodes.append(hostname)

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth_provider, protocol_version=protocol)
session = cluster.connect()

rows = session.execute("SELECT * FROM stackoverflow.movies WHERE title='Sneakers (1992)' ALLOW FILTERING")
for row in rows:
    print(row)
