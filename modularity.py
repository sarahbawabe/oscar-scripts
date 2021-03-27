import networkx as nx
import networkx.algorithms.community as nx_comm
import numpy as np
import glob
import re

z = 'z2'
z_num = 2
LOWER_BOUND = 22 #TODO: fill in
UPPER_BOUND = 35 #TODO: fill in

print("LOWER_BOUND", LOWER_BOUND)
print("UPPER_BOUND", UPPER_BOUND)

graph_file_list = glob.glob(str(z)+'/*.gexf')

modularity = []
ll = []

for file in graph_file_list:
    ## extract linking len from file name
    linking_len = re.findall('\d*\.?\d+',file)
    ll_round = round(float(linking_len[1]),2)

    if ll_round >= LOWER_BOUND and ll_round < UPPER_BOUND: # if in bounds
        print(ll_round, "is IN BOUNDS")
        if ll_round % 0.5 == 0:
            print(ll_round, "is evenly divisible by 0.5")
            ll.append(ll_round)
            G = nx.read_gexf(file)

            ## calculate communities and modularity
            communities = nx_comm.greedy_modularity_communities(G)
            mod = nx_comm.modularity(G, communities)
            modularity.append(mod)

            np.save(str(z)+'/backup/modularity_'+str(z), modularity)
            np.save(str(z)+'/backup/ll_mod_'+str(z), ll)

pairs = np.transpose(np.array([modularity, ll]))
sorted = pairs[pairs[:,1].argsort()]

np.save(str(z)+'/graph_prop/modularity_'+str(z), sorted[:,0])
np.save(str(z)+'/graph_prop/ll_mod_'+str(z), sorted[:,1])
