import glob
import re
import numpy as np

graph_file_list = glob.glob('z0/*.gexf')

ll = []
for file in graph_file_list:
    linking_len = re.findall('\d*\.?\d+',file)
    ll_round = round(float(linking_len[1]),2)
    ll.append(ll_round)

print(ll)
np.save('z0/graph_prop/ll_file-order', ll)
