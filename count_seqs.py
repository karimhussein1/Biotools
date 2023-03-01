# file handeling step
# file handeling
import os
file_path = input('Enter a file path: ')
if os.path.exists(file_path):
    print("opening the file")
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
else:
    print('The file does not exist')
    exit()

# getting the sequences in a dictionary structures {id:sequence}
seqs = {}
for line in lines:
    line=line.strip()
    if line.startswith('>'):
        words = line.split()
        name = words[0]
        seqs[name]=''
    else:
        seqs[name]= seqs[name]+line

# getting the number of sequences
print(len(seqs.keys()))
