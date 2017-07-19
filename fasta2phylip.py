#!/usr/bin/env python
import os
import argparse
from Bio import AlignIO
import sys

version = "0.1.0 (19.07.17)"
name = os.path.basename(sys.argv[0]) #get scriptname from actual script filename that was called
parser=argparse.ArgumentParser(description="Converts alignments in FastaFormat to (strict) phylip format. Will raise error if alignments contain dots (\".\"), so replace those with dashes (\"-\") beforehand (e.g. using sed)")
parser.add_argument('-i','--input', action = "store", dest = "input", required = True, help = "(aligned) input fasta")
parser.add_argument('-o','--output', action = "store", dest = "output", help = "Output filename (default = <Input-file>.phylip")
args=parser.parse_args()
if not args.output:
	args.output = args.input + ".phylip"  #if no outputname was specified set outputname based on inputname

def main():
	infile = open(args.input, "r")
	outfile = open(args.output, "w")
	alignments = AlignIO.parse(infile, "fasta")
	AlignIO.write(alignments, outfile, "phylip")
	infile.close()
	outfile.close()
	sys.stderr.write("\nfinished\n")

main()
