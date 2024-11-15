#! /usr/bin/python3
import os, sys, subprocess, re
import numpy as np
import pandas as pd

#INPUT list of accessions
accessions = ['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']
#PROCESS list of accessions
#OUTPUT the ones we want
for acc in accessions:
        print(acc)

#INPUT list of accessions
accessions = ['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']
outputs= []
#PROCESS list of accessions
for acc in accessions:
#contain the number 5
    if re.search(r'5',acc):
        outputs.append('contain the number 5: ' + acc)
#contain the letter d or e
    if re.search(r'[de]', acc):
        outputs.append('contain the letter d or e: ' + acc)
#contain the letter d and e (adjacent)
    if re.search(r'de', acc):
        outputs.append('contain the letter d and e (have to be adjacent): ' + acc)
#contain the letters d and e in that order (don't have to be adjacent, but can be)
    if re.search(r'd.*e', acc):
        outputs.append('contain the letter d and e in that order (dont have to be adjacent): ' + acc)
#contain the letters d and e in that order with a single letter in between them
    if re.search(r'd.e', acc):
        outputs.append('contain the letter d and e in that order with a single letter between them: ' + acc)
#contain both the letters d and e in any order
    if re.search(r'd', acc) and re.search(r'e', acc):
        outputs.append('contain both the letters d and e in any order: ' + acc)
#start with x or y
    if re.search(r'(^x|^y)', acc) :
        outputs.append('start with x or y: ' + acc)
#start with x or y and end with e
    if re.search(r'(^x|^y)', acc) and re.search(r'(e$)', acc):
        outputs.append('start with x or y and end with e: ' + acc)
#contains any 3 numbers in any order
    if len(re.findall(r'\d', acc)) == 3:
        outputs.append('contains any 3 numbers in any order: ' + acc)
#contains 3 different numbers
    if len(set(re.findall(f'\d', acc)))==3:
        outputs.append('contains 3 different numbers: ' + acc)
#contain 3 or more numbers in a row
    if re.search(r'\d{3, }', acc):
        outputs.append('contain 3 or more numbers in a row: ' + acc)
#end with d then either a, r or p
    if re.search(r'd[arp]$', acc):
        outputs.append('end with d followed by either a, r or p: ' + acc)

outputs.sort()
print(('\n').join(outputs))
