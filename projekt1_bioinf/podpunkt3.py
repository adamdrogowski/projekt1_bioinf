# %%
from Bio import Entrez, SeqIO

Entrez.email = "adam.drogowski.1@gmail.com"  

protein_accession = "NP_001539.3"

with Entrez.efetch(db="protein", id=protein_accession, rettype="fasta", retmode="text") as handle:
    protein_record = SeqIO.read(handle, "fasta")

print(protein_record.id)
print(protein_record.description)
print(protein_record.seq[:120]) 

SeqIO.write(protein_record, "IFIT1_protein.fasta", "fasta")
print("Zapisano plik: IFIT1_protein.fasta")