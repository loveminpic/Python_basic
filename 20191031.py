#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:34:10 2019

@author: mac
"""

about_python = """

Python is a general - purpose programming Language. It is becoming more and more
populat for doing fata science.

"""

print(about_python)

words = about_python.split() #리스트화

print(words)

print([(x.strip('.').upper(), len(x.strip('.'))) for x in words][:5]) 

