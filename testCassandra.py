from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

# initializing variable defaults
hostname="127.0.0.1"
username="cassandra"
password="cassandra"
protocol=4

#check arguments for overrides
if (len(sys.argv) > 1):
    hostname=sys.argv[1]

if (len(sys.argv) > 2):
    username=sys.argv[2]

if (len(sys.argv) > 3):
    password=sys.argv[3]

nodes = []
nodes.append(hostname)

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth_provider, protocol_version=protocol)
session = cluster.connect()

rows = session.execute("SELECT broadcast_address, host_id, data_center, rack, tokens FROM system.local; -- this is a comment\n")
for row in rows:
    print("address: " + row[0])
    print("host id: " + str(row[1]))
    print("data center: " + row[2])
    print("rack: " + row[3])
    print("tokens: " + str(len(row[4])))
