#!/usr/bin/env python
# copyright (c) 2022-2023, Karim Hussein
# this is a python script to convert DNA FASTA files to protein sequences (amino acids).

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
Frame1_translation = ""
Frame2_translation = ""
Frame3_translation = ""

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

# getting the orf of every sequence from the seqs dictionary
for seq in seqs.values():
    orf_finder(seq)

# getting all the frames in one variable
frames = frame1 + frame2 + frame3
#print(len(frames))
#print(frame1)


def translate(sequence):

    """
    translate function used to translate 5` to 3` DNA sequence to protein sequence(amino acid)

    FASTA file's orientation of DNA sequences is usually from 5` To 3`
    same as RNA synthesis direction so to convert it to RNA we replace
    the Thymine base with Uracil and use a codon table without reverse transcribtion.
    """
    codon2amino = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

    protein = ""
    if len(sequence)%3 == 0:
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            protein += codon2amino[codon]
    return protein

# taking user's input which frame to translate
orf = input("Please select which open reading frame to translate \
            \ntype 1 or 2 or 3 or press enter if you want to translate all the open reading frames \n")
f = open("translation.txt", "w")
if orf == "1":
    Frame1_translation = translate(''.join([str(elem) for i,elem in enumerate(frame1)]))
    output = ("Frame 1 translation", "\n", Frame1_translation)
    f.writelines(output)
    print("check translation.txt file")
    f.close()
    exit()
if orf == "2":
    Frame2_translation = translate(''.join([str(elem) for i,elem in enumerate(frame2)]))
    output = ("Frame 2 translation", "\n", Frame2_translation)
    f.writelines(output)
    print("check translation.txt file")
    f.close()
    exit()
if  orf == "3":
    Frame3_translation = translate(''.join([str(elem) for i,elem in enumerate(frame3)]))
    output = ("Frame 3 translation", "\n", Frame3_translation)
    f.writelines(output)
    print("check translation.txt file")
    f.close()
    exit()
else:
    Frame1_translation = translate(''.join([str(elem) for i,elem in enumerate(frame1)]))
    Frame2_translation = translate(''.join([str(elem) for i,elem in enumerate(frame2)]))
    Frame3_translation = translate(''.join([str(elem) for i,elem in enumerate(frame3)]))
    output = ("Frame 1 translation", "\n", Frame1_translation, "\n", "Frame 2 translation",\
              "\n", Frame2_translation, "\n", "Frame 3 translation", "\n", Frame3_translation)
    f.writelines(output)
    print("check translation.txt file")
    f.close()
