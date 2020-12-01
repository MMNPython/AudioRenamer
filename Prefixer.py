#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mmn
"""

import tkinter as tk
import os
from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    folder = filedialog.askdirectory()
    folder_path.set(folder)
      
def remove_current_prefix(directory):
    prefix = PrefixToRemoveEntry.get()
    for(dirpath, dirnames, filenames) in os.walk(directory):
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

def add_new_prefix(directory):
    prefix = PrefixToAddEntry.get()
    for(dirpath, dirnames, filenames) in os.walk(directory):
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

                    
def remove_current_suffix(directory):
    suffix = SuffixToRemoveEntry.get()
    length = len(suffix)
    for(dirpath, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            name, ext = os.path.splitext(file)
            if(ext == ExtensionEntry.get()):   
                if(name[-length:]) == suffix:
                    old = os.path.join(dirpath, file)
                    newName = name[:(len(name)-length)] + ext
                    new = os.path.join(dirpath, newName)
                    if(os.path.isfile(new)):
                        print("File " + new + "already exists.")
                    else:
                        os.rename(old, new)

                    
def add_new_suffix(directory):
    suffix = SuffixToAddEntry.get()
    length = len(suffix)
    for(dirpath, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            name, ext = os.path.splitext(file)
            if(ext == ExtensionEntry.get()):  
                if(name[-length:]) != suffix:
                    old = os.path.join(dirpath, file)
                    newName = name + suffix + ext
                    new = os.path.join(dirpath, newName)
                    if(os.path.isfile(new)):
                        print("File " + new + "already exists.")
                    else:
                        os.rename(old, new)


def run_prefixer():
    directory = folder_path.get()
    " remove current prefix if any "
    remove_current_prefix(directory)
    " remove current suffix if any"
    remove_current_suffix(directory)
    " add new prefix if any"
    add_new_prefix(directory)
    " add new suffix if any"
    add_new_suffix(directory)               

master = tk.Tk()    
master.title("Prefix-it")

# widgets
folder_path = StringVar()
FolderPathLabel = tk.Label(master, text="Run in Directory: ").grid(sticky = W, row=0, column = 0)
FolderPathEntry = tk.Entry(master, textvariable=folder_path).grid(row = 0, column=1)
FolderPathButton = tk.Button(master, text="Browse", command=browse_button)
FolderPathButton.grid(row=0, column=3)

ExtensionLabel = tk.Label(master, text="File extension (with '.'): ").grid(sticky = W, row = 2)
ExtensionEntry = tk.Entry(master)
ExtensionEntry.grid(row = 2, column=1)

PrefixToRemoveLabel = tk.Label(master, text="Prefix to Remove: ").grid(sticky = W, row = 4)
PrefixToAddLabel = tk.Label(master, text="Prefix to Add: ").grid(sticky = W, row = 5)
                            
PrefixToRemoveEntry = tk.Entry(master)
PrefixToAddEntry = tk.Entry(master)

PrefixToRemoveEntry.grid(row = 4, column=1)
PrefixToAddEntry.grid(row = 5, column=1)

SuffixToRemoveLabel = tk.Label(master, text="Suffix to Remove: ").grid(sticky = W, row = 6)
SuffixToAddLabel = tk.Label(master, text="Suffix to Add: ").grid(sticky = W, row = 7)

SuffixToRemoveEntry = tk.Entry(master)
SuffixToAddEntry = tk.Entry(master)

SuffixToRemoveEntry.grid(row = 6, column=1)
SuffixToAddEntry.grid(row = 7, column=1)

runButton = tk.Button(master, text="Run",command=run_prefixer)
runButton.place(x=200, y=200)

master.geometry("450x250")

master.mainloop()