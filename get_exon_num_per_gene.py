import sys
# import pandas as pd

in_gff = sys.argv[1]
exon_num = list()

with open(in_gff, 'r') as f:
    for line in f:
        line_list = line.split('\t')
        if line_list[2] == 'gene':
            if 'cnt' not in locals():
                cnt = 0
            else:
                exon_num.append(cnt)
                cnt = 0
        elif line_list[2] == 'exon':
            cnt += 1

for line in exon_num:
    print(line)

# with open(in_gff, 'r') as f:
#     for line in f:
#         line_list = line.split('\t')
#         if line_list[2] == 'gene':
#             gene_len = int(line_list[4]) - int(line_list[3])
#             s1 = pd.Series([gene_len])
#         elif line_list[2] == 'exon':


        