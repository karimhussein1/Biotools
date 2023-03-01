## Basic Python scripts to analyze fasta files
### count_seqs
- script to count the number of sequences in a fasta file

### biotools
- shell script to install the latest release of some Bioinformatics tools that i use using regular expressions

### orf_finder
- python script to find the open reading frames in a fasta file

### GC_content
- python script used to calculate the GC content of the sequences inside a fasta file
- output file is GC_content.txt

### DNA2Protein.py
- translate fasta file sequences to protein (amino acids) based on the desired open reading frame
- run the script with `python DNA2Protein.py` or `sudo chmod +x DNA2Protein.py` in Linux then `./DNA2Protein.py`
		- then enter the open reading frame you want to translate or press enter to translate all open reading frames
		- output file is translation.txt

### 6_frame_translation.py
- getting all the 6 reading frames (forward and reverse strands) from a fasta file

### reverse_comp.py
- getting the reverse complement of the sequences in a fasta file
- output file is reverse_comp.txt
