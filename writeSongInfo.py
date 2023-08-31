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

insert_table1 = """INSERT INTO song_info_by_session  
    (session_id, 
    item_in_session,
    artist_name, 
    length, 
    song) 
    VALUES (?,?,?,?,?)
"""

pStatement = session.prepare(insert_table1);

with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    #next(csvreader) # skip header
    for line in csvreader:

        session.execute(pStatement,(int(line[0]),int(line[1]),line[2],float(line[3]),line[4]))

