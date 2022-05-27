#!/usr/bin/python3

import os
import subprocess
import sys

class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

def init():
    logo = """
               _             
 ___  ___  ___| | _____ _ __ 
/ __|/ _ \/ _ \ |/ / _ \ '__|
\__ \  __/  __/   <  __/ |   
|___/\___|\___|_|\_\___|_|                                
    """
    usage = f"""{bcolors.RED}
usage   : {sys.argv[0]} <word for search>
exsample: {sys.argv[0]} password{bcolors.ENDC}
    """
    if len(sys.argv) != 2:
        print("[!]need more args... :(")
        print(usage)
        sys.exit()

    else:
        print(bcolors.WHITE,logo,bcolors.ENDC)
        print(f"{bcolors.YELLOW}[+]Your Keyword for Search: \"{sys.argv[1]}\"{bcolors.ENDC}")

        return sys.argv[1]

def directory_list():
    
    current_dir = os.getcwd()
    print(f"{bcolors.YELLOW}[*]Now you in \"{current_dir}\"{bcolors.ENDC}")
    cmd = f"find {current_dir} -type f 2> /dev/null"
    dir_list = subprocess.getoutput(cmd)
    dir_list = dir_list.rsplit("\n")

    if len(dir_list) != 0:
        print(f"{bcolors.YELLOW}[+]Finding the file from current directory{bcolors.ENDC}")
        for i in dir_list:
            print(i)

        return dir_list

    else:
        print("[!]Not Found anymore")
        sys.exit()

        
def keyword_hunt(search_word,dir_list):
    
    for i in dir_list:

        cmd = f"cat {i} | grep {search_word}"
        result = subprocess.getoutput(cmd)
        
        if result != "":
            print(f"{bcolors.WHITE}dir: {i}{bcolors.ENDC}")
            print(f"{bcolors.GREEN}{result}{bcolors.ENDC}")

def main():

    search_word = init()
    dir_list = directory_list()
    keyword_hunt(search_word,dir_list)

if __name__ == "__main__":

    main()

