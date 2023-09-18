import os
import subprocess
from joblib import Parallel, delayed

def run_csubst(aln_cds, rooted_tree, fg_text, cwd):
    command = f"csubst analyze --alignment_file {aln_cds} --rooted_tree_file {rooted_tree} --foreground {fg_text} --fg_exclude_wg no --cutoff_stat 'OCNany2spe,2.0|omegaCany2spe,5.0' --max_arity 5 --exhaustive_until 3"
    subprocess.run(command, cwd=cwd, shell=True)

def batch_run_csubst(aln_dir, tree_dir, fg_path, cwd_dir, og_list, n_jobs=2):

    Parallel(n_jobs=n_jobs)(
        delayed(run_csubst)(
            os.path.join(aln_dir, og) + '.fa',  # OG0000000.fa
            os.path.join(tree_dir, og) + '_tree.txt', # OG0000000_tree.txt
            os.path.abspath(fg_path),
            os.path.join(cwd_dir, og) # OG0000000/
        )
        for og in og_list
    )

if __name__ == '__main__':
    fg_path = '/public1/user/sifa/projects/vivipary/07_convergent_analy/foreground.txt' # foreground.txt path

    aln_dir = '/public1/user/sifa/projects/vivipary/06_downstream/trimmed_aligned_cds' # trimmed aligned cds
    tree_dir = '/public1/user/sifa/projects/vivipary/01_ortho_results/Resolved_Gene_Trees' # rooted_tree

    og_list = [og[:-3] for og in os.listdir(aln_dir)]

    cwd = '/public1/user/sifa/projects/vivipary/07_convergent_analy'

    for og in og_list:
        if not os.path.exists(os.path.join(cwd, og)):
            os.makedirs(os.path.join(cwd, og))

    batch_run_csubst(aln_dir, tree_dir, fg_path, cwd, og_list, n_jobs=20)
