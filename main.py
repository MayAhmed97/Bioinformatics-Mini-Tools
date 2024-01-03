# Bioinformatics Mini Tool - 2023
#
#?~-~-~-~-~-~-~-~-~-~-~-~#
#?-~-~-~ Content ~-~-~-~-#
#?~-~-~-~-~-~-~-~-~-~-~-~#
#? 0. Import Packages 
#? 1. Main Functions
#   1.1 MSA IDs Formatter
#   1.2 Pairwise Alignment Script
#   1.3 Multiple Sequence Alignment
#   1.4 Database Retrieval
#   1.5 Display Tree
#? 2. GUI
#   2.1 Theme Settings
#   2.2 Multiple Sequence Alignment Window
#   2.3 Pairwise Alignment Window
#   2.4 Database Retrieval Window
#   2.5 Main Window
#? 3. Program Functions
#   3.1 Program Start
#   3.2 Close Program
#   3.3 Switch Windows
#   3.4 Function Buttons
#   3.5 Program End
#?--------------------------#

#?~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~#
#?-~-~-~ 0. Import Packages ~-~-~-~#
#?~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~#

import os, subprocess
import PySimpleGUI as sg
from Bio import Phylo

#?~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~#
#?-~-~-~ 1. Main Functions ~-~-~-~-#
#?~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~#

#-------| 1.1 MSA IDs Formatter |--------#
def ids_formatter(input):
    input_list = input.splitlines()
    striped_list = list(map(str.strip, input_list))
    return ','.join(striped_list)
#----------------------------------------#

#-------| 1.2 Pairwise Alignment Script |--------#
def pwa_script(ref_path, qur_path, db_type, job_title):
    script_path = "./PWA.sh"
    try:
        # Run the script using subprocess
        subprocess.run(["bash", script_path, ref_path, qur_path, db_type, db_type[0], job_title.replace(' ','_' )], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")
    except FileNotFoundError:
        print(f"Bash script '{script_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
#------------------------------------------------#

#-------| 1.3 Multiple Sequence Alignment |--------#
def msa_script(id_numbers, db_type, job_title):
    script_path = "./MSA.sh"
    try:
        # Run the script using subprocess
        subprocess.run(["bash", script_path, id_numbers, db_type, job_title.replace(' ','_' )], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")
    except FileNotFoundError:
        print(f"Bash script '{script_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
#--------------------------------------------------#

#-------| 1.4 Database Retrieval |--------#
def db_script(id_numbers, db_type, job_title):
    script_path = "./DB.sh"
    try:
        # Run the script using subprocess
        subprocess.run(["bash", script_path, id_numbers, db_type, job_title], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")
    except FileNotFoundError:
        print(f"Bash script '{script_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
#-----------------------------------------#

#-------| 1.5 Display Tree |--------#
def display_newick_tree(newick_file):
    try:
        tree = Phylo.read(newick_file, 'newick')
        Phylo.draw(tree)
    except FileNotFoundError:
        print(f"Error: Newick file '{newick_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
#-------------------------------#

#?~-~-~-~-~-~-~-~-~-~-~-#
#?-~-~-~ 2. GUI ~-~-~-~-#
#?~-~-~-~-~-~-~-~-~-~-~-#

#------| 2.1 Theme Settings |-------#
sg.theme('lightblue3')
sg.set_options(font='Montserrat 10')
sg.set_global_icon('biotool.ico')

RED_COLOR = '#AA0E36'
GREEN_COLOR = '#0EAA50'
TITLE = ('Lato', 14, 'bold')
H1 = ('Lato', 12, 'bold')
H2 = ('Lato', 11)
P = ('Lato', 9)
#-------------------------------#

#----| 2.2 Multiple Sequence Alignment Window |----#
def create_msa_window():
    msa_layout = [
        [sg.Text("Multiple Sequence Alignment + Tree", font=TITLE)],
        [sg.HorizontalSeparator()],
        [sg.Text('Chose Type of Database ?', font=H1), sg.Radio('Nucleotide', 'g2', key='-NUC-',default=True), sg.Radio('Protein', 'g2', key='-PROT-')],
        [sg.Text('Query ID Numbers :'), sg.VerticalSeparator(), sg.Text('Job Title', font=H2), sg.Input(size=(12,3), key='-JOB_TITLE-', expand_x=True), sg.Checkbox('Tree', True, key='-TREE-')],
        [sg.Text('Add multiple number separated by Enter')],
        [sg.Multiline(size=(20,5), expand_x=True, key='-MSA_KEYS-')],
        [sg.Button('Start', key='-START_MSA-', expand_x=True, button_color=GREEN_COLOR), sg.Button("Back",key='-MAIN-')]
    ]
    return sg.Window("Bioinformatics Application - MSA View", msa_layout, element_justification='c')
#--------------------------------------------------#

#----| 2.3 Pairwise Alignment Window |----#
def create_pwa_window():
    pwa_layout = [
        [sg.Text("Pairwise Alignment", font=TITLE)],
        [sg.HorizontalSeparator()],
        [sg.Text('Chose Type of Database ?', font=H1), sg.Radio('Nucleotide', 'g1', key='-NUC-',default=True), sg.Radio('Protein', 'g1', key='-PROT-'), sg.VerticalSeparator(), sg.Text('Job Title', font=H2), sg.Input(size=(12,3), key='-JOB_TITLE-', expand_x=True)],
        [sg.Text('Reference ID Number :', font=H2), sg.Input(expand_x=True, key='-REF_ID-'), sg.FileBrowse('Select Reference', initial_folder=os.getcwd(), file_types=(("FASTA Files", "*.fasta"), ("FASTA Files", "*.fna"),), target='-REF_ID-')],
        [sg.Text('Query ID Number :', font=H2), sg.Input(expand_x=True, key='-QUR_ID-'), sg.FileBrowse('Select Query', initial_folder=os.getcwd(), file_types=(("FASTA Files", "*.fasta"), ("FASTA Files", "*.fna"),), target='-QUR_ID-')],
        [sg.Button('Start', key='-START_PWA-', expand_x=True, button_color=GREEN_COLOR), sg.Button("Back",key='-MAIN-')]
    ]
    return sg.Window("Bioinformatics Application - PWA View", pwa_layout, element_justification='c')
#-----------------------------------------#

#----| 2.4 Database Retrieval Window |----#
def create_db_window():     # 
    db_layout = [
        [sg.Text("Database Retrieval", font=TITLE)],
        [sg.HorizontalSeparator()],
        [sg.Text('Chose Type of Database ?', font=H1), sg.Radio('Nucleotide', 'g3', key='-NUC-',default=True), sg.Radio('Protein', 'g3', key='-PROT-'), sg.VerticalSeparator(), sg.Text('Job Title', font=H2), sg.Input(size=(12,3), key='-JOB_TITLE-')],
        [sg.Text('Your Accession Number :', font=H2), sg.Input(expand_x=True, key='-REF_ID-')],
        [sg.Text('You can add multiple number like this (AB12,CD34,XY56)')],
        [sg.Button('Start', key='-START_DB-', expand_x=True, button_color=GREEN_COLOR), sg.Button("Back",key='-MAIN-')]
    ]
    return sg.Window("Bioinformatics Application - DB View", db_layout, element_justification='c')
#-----------------------------------------#

#----| 2.5 Main Window |----#
def create_main_window():
    main_layout = [
        [sg.Text("Bioinformatics Mini Tools V 1.0", font=TITLE)],
        [sg.HorizontalSeparator()],
        [sg.Text(f'Hello, {os.getenv("USERNAME")} | Choose Your Tool To Start')], 
        [sg.Button('Database Retrieval', size=(12, 3), key='-DB-'), sg.Button('Pairwise Alignment', size=(12, 3), key='-PWA-'), sg.Button('Multiple Sequence Alignment', size=(12, 3), key='-MSA-')],
        [sg.Button('More Information', button_color=RED_COLOR, expand_x=True, key='-FMI-')]
    ]
    return sg.Window("Bioinformatics Application", main_layout, element_justification='c')
#---------------------------#

#?~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~#
#?-~-~-~ 3. Program Functions -~-~-#
#?~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~#

#----| 3.1 Program Start |----#
window = create_main_window()

while True:
    event, values = window.read()
#-----------------------------#

#----| 3.2 Close Program |----#
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
#-----------------------------#

#----| 3.3 Switch Windows |----#
    if event == '-PWA-':
        window.close()
        window = create_pwa_window()
    elif event == '-MSA-':
        window.close()
        window = create_msa_window()
    elif event == '-DB-':
        window.close()
        window = create_db_window()
    elif event == '-MAIN-':
        window.close()
        window = create_main_window()
#------------------------------#

#------| 3.4 Function Buttons |------#

        #----- PWA Script -----#
    if event == '-START_PWA-':
        job_title = values['-JOB_TITLE-']                   # Folder Title
        ref_path = values['-REF_ID-']                       # Reference Path
        qur_path = values['-QUR_ID-']                       # Query Path
        if values['-PROT-']:                                # Database Type
            db_type = "prot"
        else:
            db_type = "nucl"            
        pwa_script(ref_path, qur_path, db_type, job_title)
        #----- MSA Script -----#
    elif event == '-START_MSA-':
        job_title = values['-JOB_TITLE-']                   # Folder Title
        if values['-PROT-']:                                # Database Type
            db_type = "Protein"
        else:
            db_type = "Nucleotide"
        id_numbers = ids_formatter(values['-MSA_KEYS-'])    #Format AC Numbers
        newick_file = f"{job_title}/tree.newick"
        msa_script(id_numbers, db_type, job_title)
        if values['-TREE-']:                                # Check If Need Tree
            display_newick_tree(newick_file)
        #----- DB Script -----#
    elif event == '-START_DB-':
        job_title = values['-JOB_TITLE-']                   # Folder Title
        id_numbers = values['-REF_ID-'].replace(' ','' )    # IDs without Spaces
        if values['-PROT-']:                                # Database Type
            db_type = "Protein"
        else:
            db_type = "Nucleotide"
        db_script(id_numbers, db_type, job_title)
        #----- More Info -----#
    elif event == '-FMI-':
        sg.popup(title='More Information', keep_on_top=True, button_type=5)
#------------------------------------#

#----| 3.5 Program End |----#
window.close()
#---------------------------#
