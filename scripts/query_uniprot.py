#!/usr/bin/env python3

from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

def query_uniprot(limit=50):
    sparql = SPARQLWrapper("https://sparql.uniprot.org/sparql")
    sparql.setQuery(f"""
    PREFIX up: <http://purl.uniprot.org/core/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX taxon: <http://purl.uniprot.org/taxonomy/>
    
    SELECT ?protein ?label
    WHERE {{
      ?protein a up:Protein ;
               up:organism taxon:9606 ;
               rdfs:label ?label .
    }}
    LIMIT {limit}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    data = [
        {"Protein": r["protein"]["value"], "Label": r["label"]["value"]}
        for r in results["results"]["bindings"]
    ]
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = query_uniprot()
    df.to_csv("data/uniprot_results.csv", index=False)
    print("Query complete. Results saved to data/uniprot_results.csv")
