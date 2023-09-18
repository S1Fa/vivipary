import os
import argparse
from joblib import Parallel, delayed
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Seq import Seq

def paddding_cds(sequence):
    remainder = len(sequence) % 3
    if remainder == 0:
        return sequence
    else:
        return sequence + Seq('N' * (3 - remainder))


def from_cds_to_pro(input_fasta, output_fasta, trimmed_cds):
    """trim unsatified coding sequneces and translate them to protein."""
    input_file = os.path.abspath(input_fasta)
    output_file = os.path.abspath(output_fasta)
    trimmed_file = os.path.abspath(trimmed_cds)

    trimmed_cds_records = []
    translated_seq_records = []

    for seq_record in SeqIO.parse(input_file, 'fasta'):
        if seq_record.seq[0:3] == "ATG":
            padded_seq = paddding_cds(seq_record.seq)

            translated_seq = padded_seq.translate(to_stop=True)

            trans_seq_record = SeqRecord(seq=translated_seq, id=seq_record.id, description='')
            translated_seq_records.append(trans_seq_record)

            trimmed_cds_record = SeqRecord(seq=padded_seq, id=seq_record.id, description='')
            trimmed_cds_records.append(trimmed_cds_record)

    SeqIO.write(translated_seq_records, output_file, 'fasta')
    SeqIO.write(trimmed_cds_records, trimmed_file, 'fasta')

def batch_translate(cds_dir, pro_dir, trim_dir, n_jobs):
    cds_dir = os.path.abspath(cds_dir)
    pro_dir = os.path.abspath(pro_dir)
    trim_dir = os.path.abspath(trim_dir)

    if not os.path.exists(pro_dir):
       os.makedirs(pro_dir)

    if not os.path.exists(trim_dir):
       os.makedirs(trim_dir)

    cds_fasta_files = os.listdir(cds_dir)

    Parallel(n_jobs=n_jobs)(
        delayed(from_cds_to_pro)(
            os.path.join(cds_dir, fasta),
            os.path.join(pro_dir, fasta),
            os.path.join(trim_dir, fasta)
        )
        for fasta in cds_fasta_files
    )

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-i', '--input', type=str, help="the path of the input directory.")
    parse.add_argument('-o', '--output', type=str, help="the path of the output directory.")
    parse.add_argument('-p', '--trim', type=str, help="the path of the directory of trimmed cds.")
    parse.add_argument('-t', '--thread', type=int, help="the concurrent threads wanted to use.")


    args = parse.parse_args()
    batch_translate(args.input, args.output, args.trim, args.thread)