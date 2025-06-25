.PHONY: all run clean

all: run

run:
	@echo "Running SPARQL pipeline..."
	python3 scripts/query_uniprot.py

clean:
	@echo "Cleaning output..."
	rm -f data/uniprot_results.csv
