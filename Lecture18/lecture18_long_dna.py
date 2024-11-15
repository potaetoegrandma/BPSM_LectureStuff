#! /usr/bin/python3
import os, sys, subprocess, re
import numpy as np
import pandas as pd

#Opening and reading the remote file
dna=open('/localdisk/home/s2694547/Exercises/Lecture18/long_dna.txt').read().rstrip('\n')
len(dna)
dna

#cooler way to present dna on screen
print("\n".join(re.findall('.{1,60}', dna)))

BpsmI='A[GATC]TAAT'
print('BpsmI cuts at:' ,BpsmI)
#Find the sites, incrementing by 3 to account for where the enzyme cuts in the recognition sequence
for matching in re.finditer(BpsmI, dna):
    print(matching.start()+3)

#Start: open and read the file
dna=open('/localdisk/home/s2694547/Exercises/Lecture18/long_dna.txt').read().rstrip('\n')
last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
    findnum += 1
    cut_position=matching.start()+3
#Distance from the current cut site to the previous one
    fragment_size=cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
#We also have to remember the last fragment, from the last cut to the end:
    if findnum== len(list(re.finditer(BpsmI, dna))):
        fragment_size= len(dna) - last_cut
        print('Fragment size is ' + str(fragment_size))

#Doing this for both enzymes now
#First, define both enzymes sites
BpsmI= 'A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'
#Make a list to store the cut positions for both enzymes
all_cuts=[]
#Adding cut positions for BpsmI
for match in re.finditer(BpsmI, dna):
    all_cuts.append(match.start() +3)
#Adding cut positions for BpsmII
for match in re.finditer(BpsmII, dna):
    all_cuts.append(match.start() +4)

#these aren't in sequential order, so sorting them
all_cuts.sort()
all_cuts
print(all_cuts)

#Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print("Fragment " + str(counter)+' size is ' + \
            str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position
#Now the last fragment
fragment_size = len(dna) - last_cut
counter += 1
print('Fragment '+str(counter)+' size is ' +\
        str(fragment_size) +': '+str(last_cut)+' to '+str(len(dna)) )

#we have just worked out where the enzymes cut the DNA sequence,
#so all we need to do is to use the cut positions as index positions to
#substring the dna sequence string

#let's use a dictionary to store the fragment sequences
fragment_sequences= {}

#Double Digest Run
last_cut=0
counter=0
for cut_position in all_cuts:
    counter+=1
    fragment_size= cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' +\
            str(fragment_size) +': '+str(last_cut)+ ' to ' +str(cut_position) )
#Get the sequence substring
    fragment_sequences['Fragment'+str(counter)]= dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])
#Get the fragment start and end
    fragends=dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut=cut_position
#Now the last fragment
fragment_size=len(dna)- last_cut
counter+=1
print('Fragment '+str(counter)+' size is ' +\
        str(fragment_size)+': '+str(last_cut)+ ' to '+str(len(dna)))
fragment_sequences['Fragment'+str(counter)]= dna[last_cut:]
print(fragment_sequences['Fragment'+str(counter)])
fragends = dna[last_cut:][0:6]+ '...' + dna[last_cut:][-6:]
print('Fragment has ends: '+fragends)

#Show all the sequences
print(('\n########\n').join(list(fragment_sequences.values())))

#Are the fragments actually adjacent? Quick check!
#End of Fragment 1 ACGCGT should be next to 
#beginning of Fragment 2 TGAACA
#so lets use ACGCGTTGAACA as a query against our sequence
re.search(r'ACGCGTTGAACA',dna)

