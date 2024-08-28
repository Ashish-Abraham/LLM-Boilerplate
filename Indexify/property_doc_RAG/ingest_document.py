# ingest_document.py

import os
import requests
from indexify import IndexifyClient

# Initialize IndexifyClient
client = IndexifyClient()

folder_path = "data"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Upload the PDF to Indexify
        client.upload_file("pdfqa1", file_path)
        print(f"Uploaded: {filename}")

