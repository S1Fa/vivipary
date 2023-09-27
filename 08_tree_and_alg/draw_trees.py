# from Bio import SeqIO
# from Bio.SeqRecord import SeqRecord

# alg_file = "/public1/user/sifa/projects/vivipary/CODE/08_tree_and_alg/csubst_site.1SEV.fa"

# trimmed_seq_records = []

# for record in SeqIO.parse(alg_file, "fasta"):
#     new_seq = record.seq[64:67] + "------" + record.seq[120:123]
#     new_rec = SeqRecord(seq=new_seq, id=record.id, name="", description="")
#     trimmed_seq_records.append(new_rec)

# new_alg_file = "/public1/user/sifa/projects/vivipary/CODE/08_tree_and_alg/new_alg.fa"

# with open(new_alg_file, 'w') as handle:
#     SeqIO.write(trimmed_seq_records, handle, "fasta")

from ete3 import PhyloTree

alg = """
>atr|evm_27.model.AmTr_v1.0_scaffold00025.323
YNP------LEG
>atr|evm_27.model.AmTr_v1.0_scaffold00010.472
CDP------LQG
>aco|Aco001842
YDP------LEG
>aco|Aco024029
YDP------LEG
>aco|Aco024032
YDP------LEG
>pve|pveP_jg20834
YDP------LEG
>pve|pveP_jg29920
YDP------LEG
>rsi|KAF7143675.1
YDP------LQG
>ama|evm.model.AM_PacBio_hic_scaffold_13.530
YDP------LQG
>mgu|Migut.D01813.1
YNP------IEG
>ama|evm.model.AM_PacBio_hic_scaffold_27.260
YDP------LQG
>ama|evm.model.AM_PacBio_hic_scaffold_22.694
YDP------LQG
>mgu|Migut.I00183.1
YDP------LQG
>apa|evm.model.SMLO01000099.1.9
YNP------LER
>cca|Cc04_g16570
YDP------LEG
>shy|evm.model.248.48
YDP------LEG
>opu|Opuchr04_g0062350-1.1
YDP------LQG
>lsp|KRMT.ctg28.90
YDP------LQG
>sal|evm.model.scaffold8.679
YDP------SRT
>sal|evm.model.scaffold11.109
YDP------LQG
>pgr|LOC116214673
YDP------LQG
>lsp|add.KRMT.ctg62.31
YDP------FQG
>sal|evm.model.scaffold1.873
YDP------FQG
>pgr|LOC116189367
YNP------FQG
>cpe|Clo_10204
YDP------LQG
>cpe|Clo_13038
YDP------LQG
>rap|add.RAP.scaffold6.199
YDP------LLG
>rco|30138.m004069
YDP------LQG
>gra|Gorai.003G097400.1
YDP------LQG
>gra|Gorai.001G074600.1
YDP------LSG
>tca|Thecc1EG014018t1
YDP------LEG
>csi|orange1.1g015131m
YDP------LQG
>sma|add.RKTA.ctg30.14
YDP------LQG
>xgr|HPNX.ctg0036.279
YDP------LQG
>sma|add.RKTA.ctg29.2
YDP------LQG
>xgr|add.HPNX.ctg0011.73
YDP------LQG
>seed|AT3G47520.1
YDP------LQG
>ath|AT3G47520.1
YDP------LQG
>nfr|Nfr004216
FDP------LQG
>pda|PDAC_HC_CHR15T0052600.1
YNP------LQG
>nfr|Nfr021449
YDP------LQG
>pda|PDAC_HC_CHR6T0039000.1
YDP------LQG
>osa|LOC_Os08g33720.1
YNP------LEG
>osa|LOC_Os01g61380.1
YNP------LEG
>nfr|Nfr015506
YDP------LHG
>pda|PDAC_HC_CHR8T0055300.1
YDP------LHG
>osa|LOC_Os07g43700.2
YDP------LRG"""

tree_file = "/public1/user/sifa/projects/vivipary/CODE/08_tree_and_alg/OG0003766_tree.txt"

t = PhyloTree(tree_file, format=1)

t.link_to_alignment(alignment=alg, alg_format="fasta")

t.render("phylotree.pdf")