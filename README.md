# CMC-SPARQL Pipeline

## 🔬 CMC-SPARQL Pipeline: Enabling Semantically Enriched CMC Data

This project demonstrates a reusable, Python-powered data pipeline for querying biomedical ontologies (like UniProt) using SPARQL. It’s designed to enrich CMC (Chemistry, Manufacturing & Controls) datasets by connecting structured external knowledge with internal product attributes.

> 💡 This project reflects the kind of data stewardship initiatives I’ve supported in global biopharma settings—bridging structured ontology resources with operational manufacturing data to enhance data quality, consistency, and traceability.

Built with data stewardship in mind, the pipeline reflects real-world challenges in harmonizing formulation data, reducing redundancy, and aligning with FAIR principles. The included use case simulates querying human enzymes involved in sphingolipid metabolism—relevant for biologic formulations involving lipid excipients.

I built this pipeline to simulate a real-world use case: retrieving human proteins relevant to lipid metabolism from UniProt to contextualize formulation attributes in biologics development. Using SPARQLWrapper and Python, I pulled structured data into a local CSV, visualized results with Chart.js, and deployed the output to GitHub Pages for live demonstration. It's a small but powerful example of how semantic querying, when paired with FAIR data principles, can support master data harmonization and digital transformation efforts across the CMC lifecycle.

> 💡 Perfect for CMC data stewards, knowledge graph enthusiasts, and anyone working to modernize how data is captured and shared across the pharma product lifecycle.

## 📁 Project Structure - Directory Diagram

```text
cmc-sparql-template/
├── data/                     # Output files (e.g., CSV)
│   └── uniprot_results.csv
├── scripts/                  # SPARQL query logic
│   └── query_uniprot.py
├── assets/                  # Screenshots, visuals
│   └── preview.png
├── Makefile                 # Run pipeline commands
├── requirements.txt         # Python dependencies
├── README.md                # Project description + usage
└── LICENSE                  # Open source license
```

## ⚙️ Usage Instructions

You can use this template to:
- Pull publicly available data into local CSV format
- Map ontology terms to support Master Data or formulation studies
- Showcase your data stewardship skills (e.g., SPARQL, RDF, FAIR)

## ⚙️ Getting Started

Clone the repo and install requirements:
```bash
git clone https://github.com/grant-mueller/cmc-sparql-template.git
cd cmc-sparql-template
```

## 🧰 Requirements

Install required Python libraries:
```bash
pip install -r requirements.txt
```

🚀 Run the Pipeline
```bash 
make
