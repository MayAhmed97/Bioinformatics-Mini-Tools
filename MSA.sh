#!/bin/bash

#-------| Create Drectory |--------#
directory="$3"

directory_exists() {        # Check Directory Exists
    [ -d "$1" ]
}

while directory_exists "$directory"; do
    count=$((count + 1))
    directory="${directory}_${count}"
done

mkdir "$directory"
#----------------------------------#


#-------| MSA Function |--------#
efetch -db $2 -format fasta -id $1 > $directory/sequences.fasta         # Get Sequences from Database

mafft --auto $directory/sequences.fasta > $directory/msa_result.fasta   # Make MSA with MAFFT

fasttree $directory/msa_result.fasta > $directory/tree.newick           # Make Phylogenetic Tree with FastTree
#-------------------------------#


#--------| Open Files |---------#
xdg-open $directory/sequences.fasta
xdg-open $directory/msa_result.fasta
#-------------------------------#
