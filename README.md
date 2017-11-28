### fasta2phylip.py

Converts alignments in FastaFormat to (strict & interleaved; relaxed &
interleaved if '-r' is set) phylip format. Will raise error if alignments
contain dots ("."), so replace those with dashes ("-") beforehand (e.g. using
sed)

#### Dependencies:
 - python 2.7+
 - biopython

#### usage: 

````
fasta2phylip.py [-h] -i INPUT [-o OUTPUT] [-r]
````


#### optional arguments:
````
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        (aligned) input fasta
  -o OUTPUT, --output OUTPUT
                        Output filename (default = <Input-file>.phylip
  -r, --relaxed         output in "relaxed" phylip format. (default = False
                        --> Output is strict phylip
````


