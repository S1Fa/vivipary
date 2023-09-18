import os
import subprocess
from joblib import Parallel, delayed

def run_pal2nal(aligned_pep, unaligned_cds, output_file):
    command = f'pal2nal.pl {aligned_pep} {unaligned_cds} -output fasta -nogap -nomismatch > {output_file}'
    subprocess.run(command, shell=True)

def batch_run(pep_dir, cds_dir, output_dir, al_list, n_jobs=2):

    Parallel(n_jobs=n_jobs)(
        delayed(run_pal2nal)(
            os.path.join(pep_dir, og_fasta),
            os.path.join(cds_dir, og_fasta),
            os.path.join(output_dir, og_fasta)
        )
        for og_fasta in al_list
    )


if __name__ == '__main__':

    alignment_list = []

    with open('/public1/user/sifa/projects/vivipary/06_downstream/seed_ogs_with_resolved_tree.txt', 'r') as f:
        for line in f:
            alignment_list.append(line.strip()+'.fa')

    # aligned_pep_dir = '/public1/user/sifa/projects/vivipary/01_ortho_results/MultipleSequenceAlignments'
    # alignment_list = os.listdir(aligned_pep_dir)

    aligned_cds_dir = '/public1/user/sifa/projects/vivipary/06_downstream/aligned_cds'
    if not os.path.exists(aligned_cds_dir):
        os.makedirs(aligned_cds_dir)

    pep_dir = '/public1/user/sifa/projects/vivipary/06_downstream/aligned_pro_sequences'
    cds_dir = '/public1/user/sifa/projects/vivipary/06_downstream/unaligned_cds_sequences'

    batch_run(pep_dir, cds_dir, aligned_cds_dir, alignment_list, n_jobs=10)