from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

clientID=sys.argv[1]
secret=sys.argv[2]

cloud_config= {
        'secure_connect_bundle': '/home/aploetz/local/stackoverflow/secure-connect-aaronsdb.zip'
}
auth_provider = PlainTextAuthProvider(clientID, secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

name = "Aaron"
pStatement = session.prepare("SELECT movies FROM stackoverflow.fav_movies WHERE name=?");

rows = session.execute(pStatement,(name,)).one()
if rows:
    # print(rows.movies)
    movies = rows.movies
    
    for movie in movies:
    	print(movie)
    
else:
    print("An error occurred.")
