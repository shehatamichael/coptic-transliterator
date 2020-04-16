#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/14/2020

@author: michaelshehata
"""

# takes a file and returns a string of file contents

from sys import argv

script, filename = argv


def convert(filename):
	with open (filename, "r") as myfile:
		data=myfile.read()
		return data