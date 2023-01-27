# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:35:41 2023

@author: drsau
"""
from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

label_list = Label(root)
label_item = Label(root)


list_items=['Bottle','Tiffin','ID Card','Chocolates','Chips','Tickets','Hanky']
label_list["text"] = "Listed Items : " + str(list_items)



def bag_items():
    random_item = random.sample(range(1,7),1)
    label_item["text"] = "Put item no " + str(random_item) + "In Bag"
    
    

btn=Button(root,text=" Which Item To Put In Bag ?  ",command=bag_items)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

label_list.place(relx=0.5,rely=0.5,anchor=CENTER)
label_item.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()