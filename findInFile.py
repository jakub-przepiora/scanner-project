#!/usr/bin/python3 
import re

class FindVulnFunction:


    keywords_to_check = ['$_POST', '$_GET[', ' eval(', ' system(']  
    regex_patterns = [re.compile("'\.\$[a-zA-Z0-9]+\.'")]  
   
    def __init__(self, format, fileList) -> None:
        susLine = 0
        for file in fileList:
            extension = file.split('.')[1]
            if len(extension) <= 1:
                print('============================================================================')
                print(f'[!!!] Sus line: {susLine}')
                return None
            if extension in format:
                if extension == 'php':
                    susLine += self.findInPhpFile(file)
        print('============================================================================')
        print(f'[!!!] Sus line: {susLine}')     
        

    def findInPhpFile(self, dir):
        openedFile = open(dir, 'r')
        finds = 0
        for i, line in enumerate(openedFile.readlines(), start=1):
         

            for keyword in self.keywords_to_check:
                if keyword in line:
                    self.printDiscovery(i, dir, keyword, line.strip())
                    finds += 1

            for pattern in self.regex_patterns:
                if re.search(pattern, line):
                    self.printDiscovery(i, dir, pattern.pattern, line.strip())
                    finds += 1

        return finds

    def printDiscovery(self, lineNumber, dir, foundPattern, line):
        print(f'''
[-] [Line {lineNumber}][{dir}][found: {foundPattern}]: 
    {line}
''')


if __name__ == "__main__":
    print('It\'s only module to Scanner Project. Please import me :)')