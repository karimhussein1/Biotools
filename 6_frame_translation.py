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


frame1 = []
frame2 = []
frame3 = []
# frames on the reverse strand.
frame4 = []
frame5 = []
frame6 = []




# defining reverse complement function
def revcomp(sequences):
    revseq = sequences.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
    return revseq



# making a fucntion to get all reading frames on the forward strand
def orf_finder(dna):
    for i in range(0, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf1 = dna[i:stop+3]
                    if len(orf1) % 3 == 0:
                        frame1.append(orf1)
                        break
#
    for i in range(1, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf2 = dna[i:stop+3]
                    if len(orf2) % 3 == 0:
                        frame2.append(orf2)
                        break
#
    for i in range(2, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf3 = dna[i:stop+3]
                    if len(orf3) % 3 == 0:
                        frame3.append(orf3)
                        break


# getting all reading frames on the reverse strand

def orf_finder_rev(dna):
    for i in range(0, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf1 = dna[i:stop+3]
                    if len(orf1) % 3 == 0:
                        frame4.append(orf1)
                        break
#
    for i in range(1, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf2 = dna[i:stop+3]
                    if len(orf2) % 3 == 0:
                        frame5.append(orf2)
                        break
#
    for i in range(2, len(dna), 3):
        if dna[i:i+3] == 'ATG':
            for stop in range(i+3, len(dna), 3):
                if dna[stop:stop+3]=='TAA' or dna[stop:stop+3]=='TAG' or dna[stop:stop+3]=='TGA':
                    orf3 = dna[i:stop+3]
                    if len(orf3) % 3 == 0:
                        frame6.append(orf3)
                        break

for seq in seqs.values():
    orf_finder(seq)
    orf_finder_rev(revcomp(seq))



frames = frame1 + frame2 + frame3 + frame4 + frame5 + frame6
print(len(frames))
