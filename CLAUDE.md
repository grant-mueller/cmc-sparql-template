# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Run the pipeline**: `make` or `make run` - executes the SPARQL query and generates CSV output
- **Clean output**: `make clean` - removes generated CSV files
- **Install dependencies**: `pip install -r requirements.txt`
- **Run script directly**: `python3 scripts/query_uniprot.py`

## Architecture Overview

This is a Python-based SPARQL pipeline for querying biomedical ontologies, specifically designed for CMC (Chemistry, Manufacturing & Controls) data enrichment workflows.

### Core Components

- **scripts/query_uniprot.py**: Main pipeline script that queries UniProt's SPARQL endpoint for human proteins and exports results to CSV
- **data/**: Output directory for generated CSV files
- **Makefile**: Provides convenient commands for running the pipeline and cleanup

### Data Flow

1. SPARQL query targets UniProt endpoint (https://sparql.uniprot.org/sparql)
2. Queries for human proteins (taxon:9606) with labels
3. Results are processed with pandas and exported to `data/uniprot_results.csv`
4. Default query limit is 50 records but can be adjusted in the `query_uniprot()` function

### Key Dependencies

- **SPARQLWrapper**: For executing SPARQL queries against remote endpoints
- **pandas**: For data processing and CSV export

### Customization Points

- Modify the SPARQL query in `query_uniprot.py` to target different organisms, protein types, or metadata
- Adjust the record limit by changing the parameter in the `query_uniprot()` function
- Output format can be modified by changing the pandas export method