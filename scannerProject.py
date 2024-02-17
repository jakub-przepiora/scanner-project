#!/usr/bin/python3

import sys
import os
from os import listdir
from os.path import isfile, join
import subprocess
import findInFile

class ScanProject:

    def __init__(self, args) -> None:
        dirToScan = self.getFlagValue(args,'-d')
        formatsToScan = self.getFlagValue(args, '-f')
        permissionScan = self.getFlagValue(args, '-p')
        if dirToScan:
            print(''' 

 _____                                  ______          _           _   
/  ___|                                 | ___ \        (_)         | |  
\ `--.  ___ __ _ _ __  _ __   ___ _ __  | |_/ / __ ___  _  ___  ___| |_ 
 `--. \/ __/ _` | '_ \| '_ \ / _ \ '__| |  __/ '__/ _ \| |/ _ \/ __| __|
/\__/ / (_| (_| | | | | | | |  __/ |    | |  | | | (_) | |  __/ (__| |_ 
\____/ \___\__,_|_| |_|_| |_|\___|_|    \_|  |_|  \___/| |\___|\___|\__|
                                                      _/ |              
                                                     |__/               

Author: TheMrEviil
============================================================================
[*] Scanning start...''')
            self.startScan(dirToScan, formatsToScan, permissionScan)
        else:
        
            return None
    
    def getFlagValue(self, argv, flaga):
        try:
            index_flagi = argv.index(flaga)
            if index_flagi + 1 < len(argv):
                return argv[index_flagi + 1]
            else:
                print(f"Empty value flag: {flaga}")
                return True
        except ValueError:
            print(f"Flag not find {flaga} ")
            return None
        

    def getFileList(self, dir, allowed_formats=None):
        files_with_paths = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if allowed_formats is None or any(file.endswith(format) for format in allowed_formats):
                    file_path = join(root, file)
                    files_with_paths.append(file_path)
        return files_with_paths
    
    def get_php_version(self):
        try:
            result = subprocess.run(['php', '--version'], capture_output=True, text=True, check=True)
            lines = result.stdout.split('\n')
            php_version_line = lines[0]  
            php_version = php_version_line.split()[1] 
            print(f'[*] Detected PHP version: {php_version}')
            return php_version
        
        except subprocess.CalledProcessError as e:
            print(f"Error PHP not found")
            return None

    def findMostDangerousFunInFile(self, fileDir):
        
        pass

    def startScan(self, dir, format, permissions):
        php_version = self.get_php_version()
        listFilesToScan = self.getFileList(dir, format.split(','))
        findInFile.FindVulnFunction(format.split(','), listFilesToScan)
        
  
        # print(listFilesToScan)

  

if __name__ == "__main__":
    if not sys.argv[1]:
        print("You can check flags using: scanerProject.py help")
        pass
    
    if sys.argv[1] == 'help':
        
        helpFlags = ''' 
    -d      Dir start scanning
    -f      Only format (ex. php,js ...) Default get all
    -p      Check permission to file in directory
    -o      Output file
        '''
        print(helpFlags)
    
    if '-d' in sys.argv:
        ScanProject(sys.argv)
