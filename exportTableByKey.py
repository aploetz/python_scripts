from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement
import sys

# initializing variable defaults
hostname="127.0.0.1"
username="cassandra"
password="cassandra"

#check arguments for overrides
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
keyspace=sys.argv[4]
table=sys.argv[5]
#key=sys.argv[6]
#value=sys.argv[7]

nodes = []
nodes.append(hostname)

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth_provider)
session = cluster.connect()

#strCQL = f"SELECT * FROM {keyspace}.{table} WHERE {key} = ?"
strCQL = f"SELECT * FROM {keyspace}.{table}"
print(strCQL)

#statement = session.prepare(strCQL)
statement = SimpleStatement(strCQL,fetch_size=100)

#rows = session.execute(statement,value)
rows = session.execute(statement)
for row in rows:
    print(row)
