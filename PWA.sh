#!/bin/bash

#-------| Create Drectory |--------#
directory="$5"

directory_exists() {                    # Check Directory Exists
    [ -d "$1" ]
}

while directory_exists "$directory"; do
    count=$((count + 1))
    directory="${directory}_${count}"
done

mkdir "$directory"
#----------------------------------#

#-------| PWA Function |--------#
makeblastdb -in "$1" -dbtype $3                                     # Database Indexing - Reference
blast$4 -query "$2" -db "$1" > $directory/alignment_result.txt      # BLAST Query with Reference
#-------------------------------#

#--------| Open Files |---------#
xdg-open $directory/alignment_result.txt
#-------------------------------#