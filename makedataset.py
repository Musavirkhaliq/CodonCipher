import requests
from Bio import Entrez, SeqIO
import pandas as pd

# Configure Entrez
Entrez.email = "musavir119s@example.com"  # Required by NCBI

# === FUNCTIONS ===
def fetch_codon_usage(organism, protein_id):
    """Fetch codon usage table from Kazusa and save as HTML."""
    base_url = "https://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi"
    params = {"species": organism}
    r = requests.get(base_url, params=params)
    if r.status_code == 200:
        filename = f"{protein_id}_{organism.replace(' ', '_')}_codon_usage.html"
        with open(filename, "w") as f:
            f.write(r.text)
        return filename
    return None

def fetch_cDNA_from_uniprot_to_genbank(protein_id):
    """Fetch cDNA sequence for a protein via UniProt → GenBank → FASTA."""
    # Step 1: Query UniProt
    uni_url = f"https://rest.uniprot.org/uniprotkb/search?query={protein_id}&format=json"
    r = requests.get(uni_url)
    if r.status_code != 200:
        return None
    results = r.json()
    if "results" not in results or len(results["results"]) == 0:
        return None

    # Get primary accession
    accession = results["results"][0]["primaryAccession"]

    # Step 2: Map to GenBank (NCBI)
    handle = Entrez.esearch(db="nuccore", term=accession)
    record = Entrez.read(handle)
    if not record["IdList"]:
        return None
    genbank_id = record["IdList"][0]

    # Step 3: Fetch FASTA
    handle = Entrez.efetch(db="nuccore", id=genbank_id, rettype="fasta", retmode="text")
    try:
        seq_record = SeqIO.read(handle, "fasta")
    except Exception:
        return None
    fasta_file = f"{protein_id}_cDNA.fasta"
    SeqIO.write(seq_record, fasta_file, "fasta")
    return fasta_file

# === MAIN ===
def main():
    df = pd.read_csv("tpi_sequences_filtered_withcodon.csv", sep="\t", header=None)
    df.columns = ['ID', 'Number1', 'Number2', 'Description', 'Organism', 'CDNA',
       'codon usuage table']

    cDNA_files = []
    codon_files = []

    for idx, row in df.iterrows():
        protein_id = row["Protein_ID"]
        organism = row["Organism"]

        print(f"Processing {protein_id} ({organism})...")

        # Codon usage
        codon_file = fetch_codon_usage(organism, protein_id)
        codon_files.append(codon_file)

        # cDNA sequence
        fasta_file = fetch_cDNA_from_uniprot_to_genbank(protein_id)
        cDNA_files.append(fasta_file)

    df["cDNA_fasta"] = cDNA_files
    df["codon_usage"] = codon_files

    df.to_csv("data_with_sequences.csv", index=False)
    print("Saved updated CSV: data_with_sequences.csv")

if __name__ == "__main__":
    main()
