#!/

import argparse
from Bio import SeqIO


# define our functions
def get_args():
    # create an ArgumentParser object ('parser') that will hold all the information necessary to
    #parse the command line
    parser=argparse.ArgumentParser(description="Read in gff and fasta files")
    parser.add_argument("-gf",help="gff input filename" ,dest="gff_file", type=str, required=True)
    args=parser.parse_args()
    #parse the arguments
    return parser.parse_args()

def reverse_complement(open_file):
    for record in SeqIO.parse("test.fa","fasta"):
	print('reverse complement is ', record.seq.reverse_complement())



####################### Now find the reverse complement#########################
#split the tabs

#positions=line.split(\tab)
#now only grab the "+" forward lines
#f (positions[5])


#this assigns the inputs from command line -fa  as file_fasta
# -gf input as file_GFF
# these match the "dest": dest="input"
file_fasta = args.fasta_file
# from dest="output"
file_GFF = args.gff_file

#open the file for use in loop
open_file = open(file_GFF)

#BioPython to strip the header from fsa file
for record in SeqIO.parse(file_fasta, "fasta"):
    genome = record.seq

#read gff in line by line using a for loop
#split line into list,grab 4th and 5th on list, print it out to the screen, and continue to the next line, print
for line in open_file:
    positions = line.split("\t")
    start = (positions[3])
    stop = (positions[4])
    print("start codon is " + start + " and stop codon is " + stop)

#change positions to integers, pull sequence from watermelon.fsa, print
    start_2 = int(positions[3])
    stop_2 = int(positions[4])
    trimmedDNA = genome[start_2:stop_2]
    print(trimmedDNA)

def main():
    parse_GFF(open_file)
