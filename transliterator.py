#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/14/2020

@author: michaelshehata
"""

from sys import argv
import file_to_string
import coptic_translit


script, file = argv


file = file_to_string.convert(file)

print("\n--------------------------------------------------")
print("Original text:\n")
print(file)


translit_string = coptic_translit.translit(file)

print("\n--------------------------------------------------")
print("Transliterated text:\n")
print(''.join(translit_string))


print("\n--------------------------------------------------")
print("Would you like to save the transliteration as a new file?")
print("(Will create new file or truncate if already exists.)")
save = input("> ")
if save == "yes" or save == "y" or save == "Yes" or save == "Y":
	print("What would you like to call it?")
	name = input("> ")
	txt = open(name, "w")
	txt.write(translit_string)
	print("File saved.")
else:
	print("File not saved.")