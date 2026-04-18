from Bio.Seq import Seq 

with open('rosalind_ini.txt', 'r') as file:
  contents = file.read()
  sequence = Seq(contents)
  a = sequence.count("A")
  c = sequence.count("C")
  g = sequence.count("G")
  t = sequence.count("T")
  print(a, c, g, t)
