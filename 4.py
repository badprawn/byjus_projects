#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:04:08 2024

@author: pranavnair
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Project")
root.geometry("600x600")
root.config(bg = "grey")

guielements = ['Label', 'Button', 'Dropdown']
dropdown = ttk.Combobox(root, values=guielements, state="readonly")
dropdown.pack()

class elements:
    def __init__(self):
        print("This is the class for creating the GUI elements")
        
    def createLabel(self):
        label = Label(root, text = "This is the label element is created by a class", fg = "blue")
        label.pack()
    
    def createButton(self):
        btn = Button(root, text  = "This is a button element created by a class", bg = "black", fg = "white", command = self.message)
        btn.pack(padx = 30, pady = 30)
    
    def createDropdown(self):
        valuesDropdown = ['DUMMY value1', 'DUMMY value2', 'DUMMY value 3']
        dummydropdown = ttk.Combobox(root, values=valuesDropdown, state="readonly")
        dummydropdown.pack()
    def choose(self):
        global dropdown
        element = dropdown.get()
        if (element == "Label"):
            self.createLabel()
        elif (element == "Button"):
            self.createButton()
        elif (element  == "Dropdown"):
            self.createDropdown()
        else:
            print("you have not selected anything")
    def message(self):
        print("You have clicked the button created by the class.")
    
obj_of_elements = elements()
btncall = Button(root, text= "Click to create GUI elemnts on TKINTER Page.", command = obj_of_elements.choose)
btncall.pack()

root.mainloop()
        
        
        