import os

untrimmed_aln_cds = '/public1/user/sifa/projects/vivipary/06_downstream/aligned_cds'

trimmed_aln_cds = '/public1/user/sifa/projects/vivipary/06_downstream/trimmed_aligned_cds'


un_list = os.listdir(untrimmed_aln_cds)

tr_list = os.listdir(trimmed_aln_cds)

failed_list = [item for item in un_list if item not in tr_list]

with open('/public1/user/sifa/projects/vivipary/06_downstream/failed_trimming_aln_cds.txt', 'w') as f:
    for og in failed_list:
        f.write(f'{og}\n')

print(len(failed_list)) # 315