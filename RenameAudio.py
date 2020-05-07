# -*- coding: utf-8 -*-
"""
@author: Mirren Malcolm-Neale

Script to rename all audio files in current/Audio directory to keep with
desired naming convention
"""
import os

 
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories in given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    
    # Iterate over all the entries
    # If entry is a directory then get the list of files in this directory
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles     

def create_id(filename):
    name, ext = os.path.splitext(filename)
    version = 1
    return "AUD_{name}_{uid}{ext}".format(name=name, uid="v"+str(version), ext=ext)
    
 
def main():
    currentDir = os.getcwd()
    audioDir = os.path.join(currentDir, 'Audio');
        
    # Rename all files if not already appeneded with 'AUD'
    for (dirpath, dirnames, filenames) in os.walk(audioDir):
        for file in filenames:
            if (file[:4] != "AUD_" and not (os.path.isfile(file))):
                old = os.path.join(dirpath, file)
                new = os.path.join(dirpath, create_id(file))
                if(os.path.isfile(new)):
                    print("File " + new + " already exists.")
                else:    
                    os.rename(old, new)
            
if __name__ == '__main__':
    main()

