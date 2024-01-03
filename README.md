# Bioinformatics-Mini-Tools

The main codebase of the tool was developed  using bash and integrates with Python to provide a user-friendly interface that prompts for inputs and options. The tool can be started using command-line interface (CLI) and offers a graphical user interface (GUI) to handle user input. 
The GUI facilitates the processes of inputting accession numbers, uploading Fasta files, and navigating through the tool's functions. For database retrieval, the bash script uses EFetch, a widely used tool in bioinformatics for accessing and retrieving data from various biological databases. Efetch is part of the Entrez Utilities provided by the National Center for Biotechnology Information (NCBI). For pairwise alignment and multiple sequence alignment, it uses BLAST and MAFFT, respectively. For construction of phylogenetic trees, it uses FastTree. BioPython and Matplotlib libraries were used to create a visualization of the phylogenetic tree. 

# Prerequisites:


For the script to function properly, the following tools must exist on the machine the user wishes to run the script on: 
• Python Interpreter

• EFetch

• BLAST 

• MAFFT

• FastTree

Additionally for the GUI to start, the following Python package is needed: 

• Pysimple GUI

• BioPython

• Matplotlib


These resources can be downloaded on an Ubuntu or Debian-based  Linux operating system by using the following commands in the terminal (You might need different commands for other Linux distributions or different or using a different operating system): 

• sudo apt install python3

• pip3 install PySimpleGUI 

• pip3 install BioPython

• pip3 install Matplotlib

• sudo apt-get install efetch

• sudo apt-get install ncbi-blast+

• sudo apt-get install mafft

• sudo apt-get install fasttree


# Installing and Running the tool
   


a. Install the directory containing the code files, Program.

b. Locate and open the directory.

c. Run the automation script,  main.py through the command prompt by typing python main.py

d. The main prompt of the program will appear and the greeting will include the username:


e. Choose the function you would like to perform from three options: Database Retrieval Pairwise Alignment or Multiple Sequence alignment.

f. You can press More Information for guidance on how to use the tool. 



For Database Retrieval:
i. Choose the type of the database, eg.Protein

ii. Enter the Accession Number eg.AAB30713.1

iii. Enter the Job Title which will be the name of the directory into which the outputted fasta file will be installed. eg.Test

iv. Press start

v. A fasta-formatted file will be downloaded in a new directory under the name of Job title you entered. 



For Pairwise Alignment:

i. Choose the type of the database, eg.Protein

ii. Enter the Accession Number for reference sequence eg.AAB30713.1, or upload a fasta file from your local computer.

iii. enter the accession number of the query sequence. eg.XP_036255129.1, or upload a fasta file from your local computer.

iv. Enter the Job Title which will be the name of the directory into which the outputted fasta file will be installed. eg.Test

v. Press start

vi. A fasta-formatted file will be downloaded in a new directory under the name of Job title you entered. 
Note: When uploading files, the file pathway can’t contain spaces. 

For Multiple Sequence Alignment and Phylogentic Tree Construction: 

i. Choose the type of the database, eg.Protein

ii.Enter the Job Title which will be the name of the directory into which the outputted fasta file will be installed. eg.Test

iii. Enter the accession numbers for the sequences you want to align in Query ID Number, and choose whether or not you want to output a phylogenetic tree.


iv. Press start

v. A new directory with the job title you entered will be created. It will contain the output file.

vi. Find the alignment output file downloaded within the new directory in a fasta format and under the default name aligned. (msa_result.fasta)

vii. Find the phylogenetic output file downloaded within the new directory new in a newick format and under the default name tree. (tree.newick) 

viii. A visualization of the phylogenetic tree will be displayed. 


