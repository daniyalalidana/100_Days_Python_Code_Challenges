import chromadb 
from chromadb.utils import embedding_functions

ef = embedding_functions.SentenceTransformerEmbeddingFunction( model_name= "all-MiniLM-L6-v2")

collection_name = "Fruits"
client = chromadb.Client()

def main():
    try:
        collection = client.create_collection(
            name=collection_name,
            configuration= {
                'hnsw': {"space": "cosine"}
            },
            metadata={"description": "Grocery data"},
            embedding_function=ef,
        )
        texts = [
        'fresh red apples',
        'organic bananas',
        'ripe mangoes',
        'whole wheat bread',
        'farm-fresh eggs',
        'natural yogurt',
        'frozen vegetables',
        'grass-fed beef',
        'free-range chicken',
        'fresh salmon fillet',
        'aromatic coffee beans',
        'pure honey',
        'golden apple',
        'red fruit'
    ]
        
        ids = [f"food_{index+1}" for index , _ in enumerate(texts) ]

        collection.add(
            ids= ids,
            documents= texts,
            metadatas= [{"source": "grocery_store", "category": "food"} for _ in texts],
        )
        print(f"Stored {collection.count()} Collections ")

        results = collection.query(
            query_texts= ["I want something fresh and fruity"],
            n_results=3
            )


        for i, (doc, doc_id, doc_dis) in enumerate(zip(
            results["documents"][0],    # ← text
            results["ids"][0],          # ← IDs
            results["distances"][0]     # ← distances
        ), start=1):                    # ← 1 se count (0 se nahi)
            print(f"{i}  [{doc_dis:.4f}] {doc_id}  {doc}")
    except Exception as error:
        print(f"Error: {error}")




if __name__ == main():
    main()