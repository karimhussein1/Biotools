#!/bin/bash
# copyright (c) 2022-2023, Karim Hussein
# this script is used to download and install the latest versions of some Bioinformatics tools that i use.
# make this script executable by sudo chmod +x biotools.sh then run it with ./biotools.sh or sh biotools.sh

# create Bioinformaticstools directory in ~
mkdir ~/Bioinformaticstools/

# install some tools

# Downloading latest release from github automatically 
echo "Downloading and installing gatk latest release........"
cd ~/Bioinformaticstools
curl -s https://api.github.com/repos/broadinstitute/gatk/releases/latest | grep browser_download | cut -d : -f 2,3 | tr -d \" | xargs wget
unzip gatk*.zip


# sra tool kit latest release
echo "Downloading and installing sra-tools latest release........"
cd ~/Bioinformaticstools
curl -s https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit | grep "Ubuntu Linux" | cut -d = -f2 | cut -d " " -f1 | tr -d \" | xargs wget 
tar xzfv sratoolkit*.tar.gz


# IGV
echo "Downloading and installing IGV latest release......."
cd ~/Bioinformaticstools
curl -s https://software.broadinstitute.org/software/igv/download | grep "Linux" | grep "https://data.broadinstitute.org/igv/projects/downloads/"| cut -d = -f2 | cut -d \" -f2 | xargs wget
unzip IGV*.zip





# STAR
echo "Installing STAR............."
cd ~/Bioinformaticstools
git clone https://github.com/alexdobin/STAR.git
cd STAR/source
make STAR

# samtools
echo "Installing Samtools............"
cd ~/Bioinformaticstools
git clone https://github.com/samtools/samtools.git
cd ~/Bioinformaticstools/samtools
autoheader
autoconf -Wno-syntax
./configure
make

# install bcftools
echo "Installing bcftools............"
cd ~/Bioinformaticstools
git clone https://github.com/samtools/bcftools.git
cd bcftools
autoheader
autoconf -Wno-syntax
./configure
make


# Install HTSlib
echo "Installing HTSlib........."
cd ~/Bioinformaticstools
git clone https://github.com/samtools/htslib.git
cd htslib
git submodule update --init --recursive
autoreconf -i
./configure
make


# Installing picard
echo "Installing picard.........."
cd ~/Bioinformaticstools
git clone https://github.com/broadinstitute/picard.git
cd picard
./gradlew shadowJar



# Installing Bwa
echo "Installing Bwa.........."
cd ~/Bioinformaticstools
git clone https://github.com/lh3/bwa.git
cd bwa; make


# Installing bowtie2
echo "Installing bowtie2"
cd ~/Bioinformaticstools
git clone https://github.com/BenLangmead/bowtie2.git
cd bowtie2
doas make




# creat bin directory to link executables
echo "Creating bin directory and linking Bioinformatics tools in it.........."
cd ~/Bioinformaticstools/
mkdir bin
cd bin
doas ln -s ~/Bioinformaticstools/STAR STAR
doas ln -s ~/Bioinformaticstools/htslib/bgzip bgzip
doas ln -s ~/Bioinformaticstools/samtools/samtools samtools
doas ln -s ~/Bioinformaticstools/bcftools/bcftools bcftools
doas ln -s ~/Bioinformaticstools/sratoolkit*/bin/fasterq-dump fasterq-dump
doas ln -s ~/Bioinformaticstools/bowtie2/bowtie2 bowtie2
doas ln -s ~/Bioinformaticstools/bwa/bwa bwa
doas ln -s ~/Bioinformaticstools/htslib/tabix tabix
doas ln -s ~/Bioinformaticstools/bowtie2/bowtie2-build bowtie2-build
