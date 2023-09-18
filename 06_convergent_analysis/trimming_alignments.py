import os
import subprocess
from joblib import Parallel, delayed

def run_clipkit(untrimmed_aa, trimmed_aa):
    command = f'clipkit {untrimmed_aa} -o {trimmed_aa}'
    subprocess.run(command, shell=True)

def batch_run_clipkit(input_file, output_file, unaligned_list, n_jobs=2):
    Parallel(n_jobs=n_jobs)(
        delayed(run_clipkit)(
            os.path.join(input_file, fasta),
            os.path.join(output_file, fasta)
        )
        for fasta in unaligned_list
    )

def run_cdskit(seqfile, trimmed_aa_aln, outfile):
    command = f'cdskit backtrim --seqfile {seqfile} --trimmed_aa_aln {trimmed_aa_aln} --outfile {outfile}'
    subprocess.run(command, shell=True)

def batch_run_cdskit(input_file, trimmed_aa_file, output_file, og_list, n_jobs=2):
    Parallel(n_jobs=n_jobs)(
        delayed(run_cdskit)(
            os.path.join(input_file, fasta),
            os.path.join(trimmed_aa_file, fasta),
            os.path.join(output_file, fasta)
        )
        for fasta in og_list
    )

if __name__ == "__main__":
    untrimmed_aa_file = '/public1/user/sifa/projects/vivipary/06_downstream/aligned_pro_sequences'

    trimmed_aa_file = '/public1/user/sifa/projects/vivipary/06_downstream/trimmed_aligned_aa'
    if not os.path.exists(trimmed_aa_file):
        os.makedirs(trimmed_aa_file)

    untrimmed_cds_file = '/public1/user/sifa/projects/vivipary/06_downstream/aligned_cds'

    trimmed_aligned_cds = '/public1/user/sifa/projects/vivipary/06_downstream/trimmed_aligned_cds'
    if not os.path.exists(trimmed_aligned_cds):
        os.makedirs(trimmed_aligned_cds)

    og_list = os.listdir(untrimmed_aa_file)

    batch_run_clipkit(untrimmed_aa_file, trimmed_aa_file, og_list, n_jobs=10)
    batch_run_cdskit(untrimmed_cds_file, trimmed_aa_file, trimmed_aligned_cds, og_list, n_jobs=10)
