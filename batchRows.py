from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys, csv

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
session = cluster.connect("stackoverflow")

file = 'event_datafile_new.csv'

insert_table1 = """
    INSERT INTO batch_rows (local_pid, node_id, camera_id, geolocation, filepath)
    VALUES (?, ?, ?, ?, ?)
"""

pStatement = session.prepare(insert_table1);

local_pid = 219
node_id= 'P2'
camera_id= 1
geolocation= 4
filepath = 3

session.execute(pStatement,(local_pid, node_id, camera_id, geolocation, filepath))

