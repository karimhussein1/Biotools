# copyright (c) 2022-2023, Karim Hussein
# python script to find the most frequent repeat of any length in a fasta file
import os
file_path = input('Enter the path for a fasta file: ')
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
        words = line.split()
        name = words[0]
        seqs[name]=''
    else:
        seqs[name]= seqs[name]+line

def n_repeats(seq, num):
    """
    n_repeats detects the number of repeats for a specified length of bases(num) with a certain pattern and
    returns a dictionary with the repeat and it's occurrences as key:value pairs
    """
    repeatsdict = {}
    for i in range(len(seq) - num):
        rep = seq[i:i + num]
        if rep in repeatsdict.keys():
            repeatsdict[rep] += 1
        else:
            repeatsdict[rep] = 1
    return repeatsdict

# calculates repeats of length n

# merge all the sequences together
all_seqs = ""
for seq in seqs.values():
    all_seqs = all_seqs+seq

# taking user input for the repeat's length
Repeat_len = input("Please enter the length of the repeat: ")

# calling n_repeats function
repeats = n_repeats(all_seqs, int(Repeat_len))
# printing the repeats and how many times they exist
print(repeats)


# reversing the dictionary to use the max function
rev_dict = {}
for key, value in repeats.items():
    rev_dict[value] = key

print(rev_dict)

# print the most frequent sequence for the specified length
print("the maximum occurring repeat is", "\n", max(rev_dict.items()))
