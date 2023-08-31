import pinecone

# test connection/key
# silently "succeeds"
pinecone.init(api_key="ef7f7c10-456f-4bb8-afef-3c5cb6fb1103", environment="gcp-starter")

print ("SUCCESS")

# list indexes
print(pinecone.list_indexes())

index  = pinecone.Index("surveydotproduct")
#index  = pinecone.Index("surveyeuclidean")
#index  = pinecone.Index("surveycosine")

#index.upsert([
#    ("1", [-3,-3,-3,-3,-3]),
#    ("2", [-1,-1,-1,-1,-1]),
#    ("3", [0,0,0,0,0]),
#    ("4", [1,1,1,1,1]),
#    ("5", [3,3,3,3,3])
#])

print(index.describe_index_stats())

results = index.query(
    vector=[0,0,0,0,0],
    top_k=5,
    include_values=True
)

print(results)