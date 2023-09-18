import os
from Bio import SeqIO

input_dir = '/public1/user/sifa/projects/vivipary/00_data/cds'

os.chdir(input_dir)
for fasta in os.listdir(input_dir):
    for seq_record in SeqIO.parse(fasta, 'fasta'):
        if seq_record.seq[:3] != "ATG":
            print(f'{seq_record.id}')
