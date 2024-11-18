import os

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

client = NVIDIAEmbeddings(
  model="NV-Embed-QA", 
  api_key=os.environ["NVIDIA_NIMS_API_KEY"], 
  truncate="NONE", 
  )

embedding = client.embed_query("What is the capital of France?")
print(embedding)
