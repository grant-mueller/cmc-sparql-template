Project Intro
# CMC-SPARQL Pipeline

💡 This project reflects the kind of data stewardship initiatives I’ve supported in global biopharma settings—bridging structured ontology resources with operational manufacturing data to enhance data quality, consistency, and traceability.
This project demonstrates a reusable, Python-powered data pipeline for querying biomedical ontologies (like UniProt) using SPARQL. It’s designed to enrich CMC (Chemistry, Manufacturing & Controls) datasets by connecting structured external knowledge with internal product attributes.

Built with data stewardship in mind, the pipeline reflects real-world challenges in harmonizing formulation data, reducing redundancy, and aligning with FAIR principles. The included use case simulates querying human enzymes involved in sphingolipid metabolism—relevant for biologic formulations involving lipid excipients.

> 💡 Perfect for CMC data stewards, knowledge graph enthusiasts, and anyone working to modernize how data is captured and shared across the pharma product lifecycle.

## 📁 Project Structure - Directory Diagram

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



⚙️ Usage Instructions

## 🧰 Requirements

Install required Python libraries:
```bash
pip install -r requirements.txt


🚀 Run the Pipeline
make


This will:
- Query the UniProt SPARQL endpoint for human protein data
- Save the results to data/uniprot_results.csv

🌐 Publish the Output
To visualize or publish results:
- Use Chart.js or another frontend tool to visualize the data
- Copy uniprot_results.csv to your GitHub Pages site:
cp data/uniprot_results.csv ~/grant-mueller.github.io/assets/


edits, or screenshots in the `assets/` folder. Want me to help you generate the README with all of this pre-filled in a single copy-paste snippet? I can absolutely do that too.

# CMC-SPARQL PipelineThis project demonstrates a reusable, Python-powered data pipeline for querying biomedical ontologies (like UniProt) using SPARQL. It’s designed to enrich CMC (Chemistry, Manufacturing & Controls) datasets by connecting structured external knowledge with internal product attributes.
Built with data stewardship in mind, the pipeline reflects real-world challenges in harmonizing formulation data, reducing redundancy, and aligning with FAIR principles. The included use case simulates querying human enzymes involved in sphingolipid metabolism—relevant for biologic formulations involving lipid excipients.

> 💡 Perfect for CMC data stewards, knowledge graph enthusiasts, and anyone working to modernize how data is captured and shared across the pharma product lifecycle.

## 📁 Project Structure

cmc-sparql-template/
├── data/                     # Output files (e.g., CSV)/                  # SPARQL query logic
│   └── query_uniprot.py
├── assets/                  # Screenshots, visuals
│   └── preview.png
├── Makefile                 # Run pipeline commands
├── requirements.txt         # Python dependencies
├── README.md                # Project description + usage
└── LICENSE                  # Open source license

## 🧰 Requirements

Install required Python libraries:
```bash
pip install -r requirements.txt

##   Run the Pipeline
make
