#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:36:55 2020

@author: mmn
"""

import tkinter as tk
import os
from tkinter import *
from os import listdir
from os.path import isfile, join
      
def remove_current_prefix(currDir):
    prefix = PrefixToRemoveEntry.get()   
    for(dirpath, dirnames, filenames) in os.walk(currDir):
        for file in filenames:
            name, ext = os.path.splitext(file)
            if(ext == ExtensionEntry.get()):
                if(file[:len(prefix)]) == prefix and not (os.path.isfile(file)):
                    old = os.path.join(dirpath, file)
                    new = os.path.join(dirpath, file[len(prefix):])
                    if(os.path.isfile(new)):
                        print("File " + new + "already exists.")
                    else:
                        os.rename(old, new)
                    
                
def add_new_prefix(currDir):
    prefix = PrefixToAddEntry.get()  
    for(dirpath, dirnames, filenames) in os.walk(currDir):
        for file in filenames:
            name, ext = os.path.splitext(file)
            if(ext == ExtensionEntry.get()):
                if(file[:len(prefix)]) != prefix:
                    old = os.path.join(dirpath, file)
                    new = os.path.join(dirpath, prefix + file)
                    if(os.path.isfile(new)):
                        print("File " + new + "already exists.")
                    else:
                        os.rename(old, new)
                    
def remove_current_suffix(currDir):
    suffix = SuffixToRemoveEntry.get()
    for(dirpath, dirnames, filenames) in os.walk(currDir):
        for file in filenames:
            name, ext = os.path.splitext(file)
            if(ext == ExtensionEntry.get()):
                length = len(suffix)
                if(name[-length:]) == suffix:
                    old = os.path.join(dirpath, file)
                    newName = name[:(len(name)-length)] + ext
                    new = os.path.join(dirpath, newName)
                    if(os.path.isfile(new)):
                        print("File " + new + "already exists.")
                    else:
                        os.rename(old, new)
                    
def add_new_suffix(currDir):
    suffix = SuffixToAddEntry.get()
    for(dirpath, dirnames, filenames) in os.walk(currDir):
        for file in filenames:
            name, ext = os.path.splitext(file)
            if(ext == ExtensionEntry.get()):
                length = len(suffix)
                if(name[-length:]) != suffix:
                    old = os.path.join(dirpath, file)
                    newName = name + suffix + ext
                    new = os.path.join(dirpath, newName)
                    if(os.path.isfile(new)):
                        print("File " + new + "already exists.")
                    else:
                        os.rename(old, new)

def run_prefixer():
    currDir = os.path.dirname(os.path.realpath(__file__))
    " remove current prefix if any "
    remove_current_prefix(currDir)
    " add new prefix "
    add_new_prefix(currDir)
    " remove current suffix if any"
    remove_current_suffix(currDir)
    " add new suffix "
    add_new_suffix(currDir)
    return
        

master = tk.Tk()

# changing the title of our master widget      
master.title("Prefixer")

ExtensionLabel = tk.Label(master, text="File extension (with '.')").grid(row = 0)
ExtensionEntry = tk.Entry(master)
ExtensionEntry.grid(row = 0, column=1)

PrefixToRemoveLabel = tk.Label(master, text="Prefix to Remove").grid(row = 1)
PrefixToAddLabel = tk.Label(master, text="Prefix to Add").grid(row = 2)

PrefixToRemoveEntry = tk.Entry(master)
PrefixToAddEntry = tk.Entry(master)

PrefixToRemoveEntry.grid(row = 1, column=1)
PrefixToAddEntry.grid(row = 2, column=1)

SuffixToRemoveLabel = tk.Label(master, text="Suffix to Remove").grid(row = 3)
SuffixToAddLabel = tk.Label(master, text="Suffix to Add").grid(row = 4)

SuffixToRemoveEntry = tk.Entry(master)
SuffixToAddEntry = tk.Entry(master)

SuffixToRemoveEntry.grid(row = 3, column=1)
SuffixToAddEntry.grid(row = 4, column=1)

# creating a button instance
runButton = tk.Button(master, text="Run",command=run_prefixer)

# placing the button on my window
runButton.place(x=200, y=150)

#size of the window
master.geometry("400x300")

master.mainloop()