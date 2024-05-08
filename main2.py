#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:01:28 2024

@author: pranavnair
"""

class bookshelf:
    
    def __init__(self, bookname, author, price, date):
        self.bbockname = bookname
        self.bauthor = author
        self.bprice = price
        self.bdate = date

    def add_book(self):
        print("Bookname : " + self.bbockname)
        print("Author : " + self.bauthor)
        print("Price : " + self.bprice)
        print("Date : " + self.bdate)
        print("Book was added!")
    
book1 = bookshelf("Harry potter and the philosopher stone", "JK Rowling", "USD 6 Million", "04/02/0310")
print("")
book2 = bookshelf("wiMPY kID", "Jeff Kinney", "Free 0$", "2/4/2024")
book1.add_book()
book2.add_book()
    