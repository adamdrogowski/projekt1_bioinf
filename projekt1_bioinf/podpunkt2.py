# %%
from Bio import Entrez, SeqIO

Entrez.email = "adam.drogowski.1@gmail.com"  

accession = "NM_001548.5"

with Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text") as handle:
    record = SeqIO.read(handle, "fasta")

print(record.id)
print(record.description)
print(record.seq[:120])  

SeqIO.write(record, "IFIT1_nucleotide.fasta", "fasta")
print("Zapisano plik: IFIT1_nucleotide.fasta")