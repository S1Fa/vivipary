import os
import subprocess
from joblib import Parallel, delayed


def run_mafft(input_file, output_file):
    mafft_command = f'mafft --auto --amino {input_file} > {output_file}'
    subprocess.run(mafft_command, shell=True)

def batch_mafft(input_dir, output_dir, og_list, n_jobs=2):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    Parallel(n_jobs=n_jobs)(
        delayed(run_mafft)(
            os.path.join(input_dir, input_file) + '.fa',
            os.path.join(output_dir, input_file) + '.fa'
        )
        for input_file in og_list
    )

if __name__ == '__main__':

    og_list = []
    with open('/public1/user/sifa/projects/vivipary/06_downstream/seed_ogs_with_resolved_tree.txt', 'r') as f:
        for og in f:
            og_list.append(og.strip())

    input_dir = '/public1/user/sifa/projects/vivipary/01_ortho_results/Orthogroup_Sequences'
    output_dir = '/public1/user/sifa/projects/vivipary/06_downstream/aligned_pro_sequences'

    batch_mafft(input_dir, output_dir, og_list, n_jobs=15)