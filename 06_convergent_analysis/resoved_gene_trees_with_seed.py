import os

files_list = os.listdir('/public1/user/sifa/projects/vivipary/01_ortho_results/Resolved_Gene_Trees')

print(len(files_list)) # 20382
# print(files_list[0][:9])

fine_named_files = [x[:9] for x in files_list]

result_ogs_lists = []

with open('/public1/user/sifa/projects/vivipary/06_downstream/ogs_with_seed.txt', 'r') as f:
    for line in f:
        if line.strip() in fine_named_files:
            result_ogs_lists.append(line.strip())

print(len(result_ogs_lists)) # 609

with open('/public1/user/sifa/projects/vivipary/06_downstream/seed_ogs_with_resolved_tree.txt', 'w') as f:
    for i in result_ogs_lists:
        f.write(f'{i}\n')
