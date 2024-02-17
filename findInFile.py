#!/usr/bin/python3 
import re

class FindVulnFunction:

    def __init__(self, format, fileList) -> None:

        # print(format)
        susLine = 0
        for file in fileList:
            extension = file.split('.')[1]
            if extension in format:
                if extension == 'php':
                    susLine += self.findInPhpFile(file)
                
        print(f'[!!!] Sus line: {susLine}')     
        

    def findInPhpFile(self, dir):
        openedFile = open(dir, 'r')
        finds = 0
        for i, line in enumerate(openedFile.readlines(), start=1):
            keywords_to_check = ['$_POST', 'eval(', 'system(']  
            regex_patterns = [re.compile(r'\.\$[^\'".]+\.')]  

            for keyword in keywords_to_check:
                if keyword in line:
                    self.printDiscovery(i, dir, keyword, line.strip())
                    finds += 1

            for pattern in regex_patterns:

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