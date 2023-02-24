# copyright (c) 2022-2023, Karim Hussein

# file handeling
import os
file_path = input('Enter a file path: ')
if os.path.exists(file_path):
    print("opening the file")
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
else:
    print('The file does not exist')


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


frame1 = []
frame2 = []
frame3 = []
# making a fucntion to get all reading frames on the forward strand
def orf_finder(dna):
    # getting the first reading frame
    for i in range(0, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf1 = dna[i:stop+3]
                    if len(orf1) % 3 == 0:
                        frame1.append(orf1)
                        break
#
    # getting the second reading frame 
    for i in range(1, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf2 = dna[i:stop+3]
                    if len(orf2) % 3 == 0:
                        frame2.append(orf2)
                        break
#
    # getting the third reading frame
    for i in range(2, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf3 = dna[i:stop+3]
                    if len(orf3) % 3 == 0:
                        frame3.append(orf3)
                        break

# getting the orf for every sequence in the seqs dictionary
for seq in seqs.values():
    orf_finder(seq)

frames = frame1 + frame2 + frame3
print(len(frames))
#print(frames)
