from Bio import Entrez, SeqIO
from datetime import date
from Bio.SeqIO import FastaIO

# overview
# query entrez using entry id, get back the sequence as fasta
# get length of the sequence
# repeat for all of the entry ids

Entrez.email = "rsrchen0@gmail.com"

with open("rosalind_frmt.txt", "r") as file:
    contents = file.read()
    entry_ids = contents.split()
    s = ""
    for i, id in enumerate(entry_ids):
        if i < len(entry_ids) - 1:
            s = s + id + ", "
        else:
            s = s + id

    handle = Entrez.efetch(db="nucleotide", id=[s], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    shortest_length = 9999999999999
    shortest_record_index = 0
    i = 0
    for i, record in enumerate(records):
        l = len(record)
        if l < shortest_length:
            shortest_length = l
            shortest_record_index = i
    
    print(records[shortest_record_index].format("fasta"))
    
    
