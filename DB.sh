#!/bin/bash

#-------| Create Drectory |--------#
directory="$3"

directory_exists() {                    # Check Directory Exists
    [ -d "$1" ]
}

while directory_exists "$directory"; do
    count=$((count + 1))
    directory="${directory}_${count}"
done

mkdir "$directory"
#----------------------------------#

#-------| DB Function |--------#
efetch -db $2 -format fasta -id $1 > $directory/sequences.fasta        #Download Sequence(s) from Database
#------------------------------#

#--------| Open Files |---------#
xdg-open $directory/sequences.fasta
#-------------------------------#