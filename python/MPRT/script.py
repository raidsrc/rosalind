from Bio import Entrez, SeqIO
import re

Entrez.email = "rsrchen0@gmail.com"
with open("rosalind_mprt.txt", "r") as file:
    contents = file.read()
    entry_ids = contents.split()
    entry_ids_before_1st_underscore = [id.split("_")[0] for id in entry_ids]
    s = ""
    for i, id in enumerate(entry_ids_before_1st_underscore):
        if i < len(entry_ids_before_1st_underscore) - 1:
            s = s + id + ", "
        else:
            s = s + id


    # need to only use the part before the first underscore (bruh)

    handle = Entrez.efetch(db="protein", id=[s], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    answers = {}

    for i, record in enumerate(records):
        id_to_use_in_final_answer = f"{entry_ids[i]}"
        answers[id_to_use_in_final_answer] = []
        results = re.finditer("(?=N[^P][ST][^P])", str(record.seq))
        for result in results:
            if result:
                index_of_motif = result.start()
                answers[id_to_use_in_final_answer].append(index_of_motif + 1)


# ugh that was painful (not really)
# now to format the output

for k, v in answers.items():
    if len(v) > 0:
        print(k)
    for number in v:
        print(number, end=" ")
    print()

"""
fetch fasta of all proteins using entrez 
scan through each record sequence char by char looking for the n-glycosylation motif as regex that's N - anything but P - S or T - anything but P
note down the indices where found 
"""
