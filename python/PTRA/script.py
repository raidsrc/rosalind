from Bio.Seq import Seq
from Bio.Seq import translate

output = ""
with open("rosalind_ptra.txt", "r") as file:
    contents = file.read().split()
    dna = Seq(contents[0])
    protein_correct = Seq(contents[1])
    genetic_code_variant_numbers = list(range(1, 34))
    genetic_code_variant_numbers.remove(7)
    genetic_code_variant_numbers.remove(8)
    genetic_code_variant_numbers.remove(17)
    genetic_code_variant_numbers.remove(18)
    genetic_code_variant_numbers.remove(19)
    genetic_code_variant_numbers.remove(20)

    protein_variants = {}
    for variant in genetic_code_variant_numbers:
        protein = translate(sequence=dna, table=f"{variant}", to_stop=False, stop_symbol="")
        protein_variants[f"{variant}"] = protein

    for i, protein_variant in protein_variants.items():
        output += i + "\n"
        output += protein_variant + "\n"
        if protein_variant == protein_correct:
            print(i, protein_variant)
    
with open("rosalind_ptra_2.txt", 'w') as file:
    file.write(str(output))