import os
import sys
import re

def change_path():
    """
    Change the directory in the system terminal
    """
    #python3 -m doctest read_music.py
    if os.name in ('nt', 'dos'):
        sys.exit("can't do this in windows. Use Linux")
    os.chdir('..')
    os.system('ls')
    path_directory = input("cd into path: ")
    get_current_working_directory = os.getcwd()
    dir_tmp = get_current_working_directory + "/" + path_directory
    print(dir_tmp)
    os.chdir(dir_tmp)
    

def read_from_file(filename):
    """
    input a filename and read
    """
    try:
        fopen = open(filename,'r')
    except:
        print("error")
    else:
        find_from_file(fopen, 'title')

def find_from_file(fopen, keywords):
    for line in fopen:
        # print(line)
        tmp = re.findall(r'<div class="lyrics-container">',line)
        if len(tmp) > 0:
            print(tmp)


if __name__ == '__main__':
    change_path()
    filename = "file.txt"
    os.system(f'ls > ../my_lib/{filename}')
    read_from_file("andrea_bocelli-the_prayer.html")
    # os.system(f'rm ../my_lib/{filename}')
    #[x]get directory
    #[x]get list of files in the directory
    #[]extract info for the model
        #[]title
        #[]video_url
        #[]lyrics
    #create the data with extracted info for database
    #write test for these
