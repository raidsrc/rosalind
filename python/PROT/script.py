from Bio.Seq import Seq

with open("rosalind_prot.txt", "r") as file:
    s = file.read()
    rna = Seq(s)
    protein = rna.translate()
    print(protein)
