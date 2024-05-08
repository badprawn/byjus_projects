#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:56:08 2024

@author: pranavnair
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Canvas")
root.geometry("700x700")

color_label = Label(root, text = "Enter a color : ")
color_label.place(relx = 0.5, rely = 0.9, anchor=CENTER)

input_box = Entry(root)
input_box.insert(0,"black")
input_box.place(relx = 0.5, rely = 0.9, anchor=CENTER)

canvas = Canvas(root, width = 590, height = 510, bg = "white", highlightbackground="lightgrey")
canvas.pack()

img = ImageTk.PhotoImage(Image.open ("start_point1.png"))
my_image = canvas.create_image(100,100,image=img)

direction = ""
oldx = 50
oldy = 50
newx = 51
newy = 51


def draw( direction, oldx, oldy, newx, newy):
    fill_color= input_box.get()
    if (direction == "right"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width = 10, fill = fill_color)
    if (direction == "left"):
        left_line = canvas.create_line(oldx, oldy, newx, newy, width = 10, fill = fill_color)
    if (direction == "up"):
        up_line = canvas.create_line(oldx, oldy, newx, newy, width = 10, fill = fill_color)
    if (direction == "down"):
        down_line = canvas.create_line(oldx, oldy, newx, newy, width = 10, fill = fill_color)
        
    
def right_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx=newx+1
    direction = "right"
    draw(direction, oldx, oldy, newx, newy)

def left_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldy = newy
    newx=newx-1
    direction = "left"
    draw(direction, oldx, oldy, newx, newy)

def up_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy-1
    direction = "up"
    draw(direction,oldx, oldy, newx, newy)

def down_dir(event):
    global oldx
    global oldy
    global newx
    global newy
    olx = newx
    oldy = newy
    newy = newy+1
    direction = "down"
    draw(direction, oldx, oldy, newx, newy)
    

root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()