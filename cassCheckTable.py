from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import sys

hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
keyspace=sys.argv[4]
table=sys.argv[5]

nodes = []
nodes.append(hostname)

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth_provider)
session = cluster.connect(keyspace)

pStatement = session.prepare("""
    SELECT column_name FROM system.schema_columns WHERE keyspace_name=? AND columnfamily_name=?;
""")

rows = session.execute(pStatement,[keyspace,table])
for row in rows:
    print row[0]
