# copyright (c) 2022-2023, Karim Hussein

# file handeling step
import os
file_path = input('Enter a file path: ')
if os.path.exists(file_path):
    print("opening the file")
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
else:
    print('The file does not exist')
    exit()

seqs = {}
for line in lines:
    line=line.strip()
    if line.startswith('>'):
        name = line
        seqs[name]=''
    else:
        seqs[name]= seqs[name]+line

def revcomp(sequences):
    reversecomp = {}
    for iD, sequence in sequences.items():
        revseq = sequence.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
        reversecomp[iD] = revseq.upper()
    return reversecomp

reverse_fasta = revcomp(seqs)

# print the reverse complement of the fasta file
print(reverse_fasta)

# print only the reversed sequences
f = open("reverse_complement.txt", "w")
for iD, seq in reverse_fasta.items():
    print(iD, "\n", seq)
    f.write(iD)
    f.write("\n")
    f.write(seq)
    f.write("\n")
f.close()
