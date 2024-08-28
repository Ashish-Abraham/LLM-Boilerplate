# setup_extraction_graph.py

from indexify import ExtractionGraph, IndexifyClient

client = IndexifyClient()

extraction_graph_spec = """
  name: 'pdfqa1'
  extraction_policies:
    - extractor: 'tensorlake/paddleocr_extractor' 
      name: 'textextract'
    - extractor: 'tensorlake/chunk-extractor'
      name: 'chunker'
      input_params:
          chunk_size: 1000
          overlap: 100
      content_source: 'textextract'
    - extractor: 'tensorlake/minilm-l6'
      name: 'pdfembedding'
      content_source: 'chunker'
"""

extraction_graph = ExtractionGraph.from_yaml(extraction_graph_spec)
client.create_extraction_graph(extraction_graph)
