#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:12:06 2024

@author: pranavnair
"""

from tkinter import *
from random import Random
root = Tk()
root.title("Random Countries & Cpitals")
root.geometry("500x900")


cityname = []
countryname = []

def displayNames():
    city_input_text = city_input.get()
    country_input_text = country_input.get()
    cityname.append(city_input_text)
    countryname.append(country_input_text)
    display_country_name['text'] = countryname
    display_city_name['text'] = cityname
    

country_input = Entry(root)
country_input.pack()
city_input = Entry(root)
city_input.pack()
displaybtn = Button(root, text = "Display Country & City Name", command = displayNames)
displaybtn.pack()
display_country_name = Label(root)
display_country_name.pack()
display_city_name = Label(root)
display_city_name.pack()
display_randomly_btn = Button(root, text = "Display Country & City Randomly")
display_random_number_for_country = Label(root)
display_random_number_for_country.pack()
display_random_number_for_city = Label(root)
display_random_number_for_city.pack()

root.mainloop()