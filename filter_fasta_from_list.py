#!/

#import modules
import argparse
from Bio import SeqIO

# define our functions
def get_args():
    # create an ArgumentParser object ('parser') that will hold all the information necessary to
    #parse the command line
    parser = argparse.ArgumentParser(description = "The file you wish to filter")

    #define positional arguments
    parser.add_argument("num", help = "The cut off length, which will cut off all sequences longer than that number", type = int)

    # define optional arguments
    parser.add_argument("-q", "--quiet", help = "Print quiet output", action = 'store_true')

    # parse the arguments
    return parser.parse_args()

short_sequences = [] # Setup an empty list
for record in SeqIO.parse("cor6_6.gb", "genbank"):
    if len(record.seq) < 300 :
        # Add this record to our list
        short_sequences.append(record)

print("Found %i short sequences" % len(short_sequences))

SeqIO.write(short_sequences, "short_seqs.fasta", "fasta")
