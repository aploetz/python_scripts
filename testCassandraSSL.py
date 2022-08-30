from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
#from OpenSSL import SSL, crypto
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED

import sys

# initializing variable defaults
hostname="127.0.0.1"
username="cassandra"
password="cassandra"
hostCertPath="/Users/aaronploetz/local/astraMigration/ca.crt"
clientKeyPath="/Users/aaronploetz/local/astraMigration/key"
clientCertPath="/Users/aaronploetz/local/astraMigration/cert"

#check arguments for overrides
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]

nodes = []
nodes.append(hostname)

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.load_verify_locations(hostCertPath)
ssl_context.verify_mode = CERT_REQUIRED
ssl_context.load_cert_chain(
    certfile=clientCertPath,
    keyfile=clientKeyPath)

auth_provider = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(contact_points=nodes,
                  port=29042,
                  auth_provider=auth_provider,
                  ssl_context=ssl_context)
session = cluster.connect()

rows = session.execute("SELECT key FROM system.local;")
for row in rows:
    print(row[0])
