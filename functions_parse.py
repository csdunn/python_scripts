#!/

import argparse
from Bio import SeqIO


# define argparse
def get_args():
    # create an ArgumentParser object ('parser') that will hold all the information necessary to
    #parse the command line
    parser=argparse.ArgumentParser(description="Read in gff and fasta files")
    parser.add_argument("-gf",help="gff input filename" ,dest="gff_file", type=str, required=True)
    args=parser.parse_args()
    #parse the arguments
    return parser.parse_args()

#define reverse_complement
def reverse_complement(open_file):
    for record in SeqIO.parse("test.fa","fasta"):
    print("reverse complement is ",record.seq.reverse_complement)

#define parse.GFF


#this assigns the inputs from command line -fa  as file_fasta
# -gf input as file_GFF
# these match the "dest": dest="input"
file_fasta = args.fasta_file
# from dest="output"
file_GFF = args.gff_file

#open the file for use in loop
open_file = open(file_GFF)

for (open_file):
    positions=line.split(\tab)

#now only grab the "+" forward lines
if open_file:
    positions[5] = "+"
then reverse_complement(open_file)




#define main
def main():
    parse_GFF(open_file)
