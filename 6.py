#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:00:39 2024

@author: pranavnair
"""

from tkinter import *
root = Tk()
root.geometry("700x700")
root.title("Percentage Clac")

percentage_grade_3_label = Label(root)
percentage_grade_5_label = Label(root)
percentage_grade_10_label = Label(root)
percentage_grade_3_label.place(relx = 0.5, rely = 0.3)
percentage_grade_5_label.place(relx = 0.5, rely = 0.6)
percentage_grade_10_label.place(relx = 0.5, rely = 0.9)

class percentage_grade_3():
    def __init__(self, languagearts, mathematics):
        self.languagearts = languagearts
        self.mathematics = mathematics
        
    def calculation(self):
        total_marks = self.languagearts + self.mathematics
        percentage = (total_marks * 100) / 200
        percentage_grade_3_label['text'] = "Percentage : " + str(percentage) + "%" 
 
obj_grade_3 = percentage_grade_3(90,45)
btn = Button(root, text = "Percentage grade 3", command=obj_grade_3.calculation)
btn.place(relx = 0.5, rely = 0.1)

class percentage_grade_5():
    def __init__(self, languagearts, mathematics, science):
        self.languagearts = languagearts
        self.mathematics = mathematics
        self.science = science
        
    def calculation(self):
        total_marks = self.languagearts + self.mathematics + self.science
        percentage = (total_marks * 100) / 300
        percentage_grade_5_label['text'] = "Percentage : " + str(percentage) + "%" 
 
obj_grade_5 = percentage_grade_5(90,45,100)
btn = Button(root, text = "Percentage grade 5", command=obj_grade_5.calculation)
btn.place(relx = 0.5, rely = 0.5)

class percentage_grade_10():
    def __init__(self, languagearts, mathematics, science, insoc):
        self.languagearts = languagearts
        self.mathematics = mathematics
        self.science = science
        self.insoc = insoc
        
    def calculation(self):
        total_marks = self.languagearts + self.mathematics + self.science + self.insoc
        percentage = (total_marks * 100) / 400
        percentage_grade_10_label['text'] = "Percentage : " + str(percentage) + "%" 
 
obj_grade_10 = percentage_grade_10(90,45,86, 75)
btn = Button(root, text = "Percentage grade 10", command=obj_grade_10.calculation)
btn.place(relx = 0.5, rely = 0.8)

root.mainloop()
    