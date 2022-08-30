from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

clientID=sys.argv[1]
secret=sys.argv[2]
secureBundleLocation=sys.argv[3]

cloud_config= {
        'secure_connect_bundle': secureBundleLocation
}
auth_provider = PlainTextAuthProvider(clientID, secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select cluster_name from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
