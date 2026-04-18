from Bio import Entrez
from datetime import date

with open("rosalind_gbk.txt", "r") as file:
    lines = []
    for line in file:
        lines.append(line)
    genus = str(lines[0]).strip()

    date1 = str(lines[1]).strip()
    date1split = date1.split("/")
    d1y = int(date1split[0])
    d1m = int(date1split[1])
    d1d = int(date1split[2])
    date1 = date(d1y, d1m, d1d)
    mindate = date1.strftime("%Y/%m/%d")

    date2 = str(lines[2]).strip()
    date2split = date2.split("/")
    d2y = int(date2split[0])
    d2m = int(date2split[1])
    d2d = int(date2split[2])
    date2 = date(d2y, d2m, d2d)
    maxdate = date2.strftime("%Y/%m/%d")

    Entrez.email = "rsrchen0@gmail.com"
    handle = Entrez.esearch(db="nucleotide", term=f'"{genus}"[Organism] AND "{mindate}"[PDAT] : "{maxdate}"[PDAT]')
    data = Entrez.read(handle)
    print(data["Count"]) # type: ignore
    
