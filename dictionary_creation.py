# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:54:00 2021

@author: user
"""
import tkinter as tk
from tkinter import *
import re
import string
from collections import Counter
import numpy as np
import nltk
#nltk.download('punkt')
from nltk import word_tokenize 
from nltk.util import ngrams


# Program for spell checking
def read_corpus(filename):
  with open(filename, "r") as file:
    lines = file.readlines()
    words = []
    for line in lines:
      words += re.findall(r'\w+', line.lower())

  return words


words = read_corpus('Zoology.txt')
print(words)

f=open("dictionary.txt","a")
for word in words:
    f.write(word+"\n")
f.close()