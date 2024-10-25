#!/usr/bin/python
#A short python script

#Calculating the A+T content
#Adding the DNA sequence
dna_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#Total sequence length
dna_seq_length=len(dna_seq)
#count number of A
count_A= dna_seq.count('A')
#count number of T
count_T=dna_seq.count('T')
#count A+T
count_AT= ((int(count_A) + int(count_T))/dna_seq_length)
#output
print("###Counts of A and T and A+T###\n","Count_A:", count_A,"\n", "Count_T:", count_T,"\n", "Count A + T:",(int(count_A) + int(count_T)))
print ("###Calculating A+T content###\n","The A+T content for the short sequence", dna_seq, "is:", count_AT)
print("The A+T content in percentage is:", count_AT*100, "percent(%)")

#Complementing DNA
dna_seq_2="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#forming pairing of ATGC
replacement1=dna_seq_2.replace('A','t')
replacement2=replacement1.replace('T','a')
replacement3=replacement2.replace('G','c')
replacement4=replacement3.replace('C','g')
#output
print("###Complement DNA sequence \n", "The complementary DNA sequence for", dna_seq, "is:", str(replacement4.upper()))

#Restriction fragment lengths
dna_seq_3="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length=dna_seq_3.find("GAATTC") + 1 #fragment before the restriction at G*AATTC motif, cut at asterisk
frag2_length=len(dna_seq_3)-frag1_length #fragment after the restriction at G*AATTC motif, cut at asterisk
#output
print("###We performed the restriction digestion and the fragment lengths are as follows###")
print("Length of fragment one is:", str(frag1_length))
print("Length of fragment two is:", str(frag2_length))

#Splicing out introns
dna_seq_4="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1=dna_seq_4[0:63]
exon_2=dna_seq_4[90: ]
intron=dna_seq_4[63:90]
coding_sequence= exon_1 + exon_2
#outputting the exons and printing the coding sequence
print("###Exons joined###\n","Exon 1:", exon_1,"\n","Exon 2:", exon_2, "\n","Coding sequence:", coding_sequence)
#calculating coding percentage of the given sequence
coding_length = len(coding_sequence)
total_length = len(dna_seq_4)
#output
print("###coding_percentage(rounded off)###\n" + str(int((coding_length/total_length)*100)))
print("###EXONintronEXON###\n","Exons are in uppercase, intron is in lowercase \n", exon_1, intron.lower(), exon_2)


#Just for fun!
print("###THAT'S IT FROM US###\n", "Thank you for using this script! Hope you had fun!! :D")

