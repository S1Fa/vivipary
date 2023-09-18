import os
from Bio import SeqIO

def extract_ids_from_fasta(fasta_file):
    """
    从FASTA文件中解析基因名称, 并返回ids_list。
    """
    ids_list = []
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):
        ids_list.append(seq_record.id)
    return ids_list

def extract_genes_by_name(gene_ids, record_dict, output_fasta_path):
    """
    根据目标基因名称从输入FASTA文件中提取基因, 并将结果保存到输出FASTA文件中。
    """
    matching_records = []
    for gene in gene_ids:
        matching_records.append(record_dict[gene])

    with open(output_fasta_path, 'w') as output_fasta:
        SeqIO.write(matching_records, output_fasta, 'fasta')


# Orthogroup_Sequences 目录路径
ortho_sequence_path = '/public1/user/sifa/projects/vivipary/01_ortho_results/MultipleSequenceAlignments'
unaligned_cds_seq_dir = '/public1/user/sifa/projects/vivipary/06_downstream/unaligned_cds_sequences'
all_cds_fasta_file = '/public1/user/sifa/projects/vivipary/06_downstream/cds_all_in_one.fasta'

# 有 seed 有 resolved 树
record_file = '/public1/user/sifa/projects/vivipary/06_downstream/seed_ogs_with_resolved_tree.txt'
record_list = []
with open(record_file, 'r') as f:
    for line in f:
        record_list.append(line.strip()) # OG ids 提取到list里
# print(len(record_list)) # return 615
record_dict = SeqIO.to_dict(SeqIO.parse(all_cds_fasta_file, 'fasta')) # {id: seq_record}

for og in record_list:
    og_path = os.path.join(ortho_sequence_path, og) + '.fa'
    output_fasta_path = os.path.join(unaligned_cds_seq_dir, og) + '.fa'

    gene_ids = extract_ids_from_fasta(og_path)
    extract_genes_by_name(gene_ids, record_dict, output_fasta_path)
