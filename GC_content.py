# copyright (c) 2022-2023, Karim Hussein
import os
file_path = input('Enter a file path: ')
if os.path.exists(file_path):
    print("opening the file")
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
else:
    print('The file does not exist')

seqs = {}
for line in lines:
    line=line.strip()
    if line.startswith('>'):
        words = line.split()
        name = words[0]
        seqs[name]=''
    else:
        seqs[name]= seqs[name]+line

def gc_content(sequences):
    """calculating gc content of a fasta file"""
    GCcontent = {}
    for Id, Seq in sequences.items():
        GCcontent[Id] = str(round(Seq.count("G") + Seq.count("C") / len(Seq) * 100, 3)) + '%'
    return GCcontent


GC_content = gc_content(seqs)
print(GC_content)
