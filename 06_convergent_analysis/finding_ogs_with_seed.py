import pandas as pd

file_path = "/public1/user/sifa/projects/vivipary/01_ortho_results/Orthogroups/Orthogroups.GeneCount.tsv"

output_file = "/public1/user/sifa/projects/vivipary/06_downstream/ogs_with_seed.txt"


# ogs_gene_counts
df = pd.read_csv(file_path, sep='\t')


filt = (df["Ath_seed"]>=1) & (df["nfr"]>=1) & (df["rap"]>=1) & (df["ama"]>=1) & (df["aco"]>=1)

results_list = df[filt]['Orthogroup'].to_list()

print(len(results_list)) # 609

with open(output_file, 'w') as fw:
    for i in results_list:
        fw.write(f'{i}\n')
