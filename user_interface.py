# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:04:57 2020

@author: Rico
"""

import code_labeller
from tkinter import *
from math import *
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x190')
        #self.entry = tk.Entry(self)
        #self.entry.place(width=400, height=500)
       
        self.txt = scrolledtext.ScrolledText(self,width=60,height=10)
        self.txt.grid(column=0,row=0)
        
        self.button = tk.Button(self, text="Predict tags", command=self.on_button)
        self.button.grid(column=0,row=1)
        #self.entry.pack()
        self.labels = []
    
    def on_button(self):
        out = code_labeller.test(self.txt.get('1.0', 'end-1c'))
        #for label in self.labels:
        #    label.destroy()
        #label = Label(self, text=str(','.join(out)))
        #self.labels.append(label)
        #label.pack()
        messagebox.showinfo('Tags for the code are:', str(','.join(out)))

app = SampleApp()
app.mainloop()