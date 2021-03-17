import networkx as nx
import numpy as np
import glob
import re

LOWER_BOUND = 16
z = 'zp5'
z_num = 0.5
graph_file_list = glob.glob(str(z)+'/*.gexf')

c_bar = []
ll = []

for file in graph_file_list:
    ## extract linking len from file name
    linking_len = re.findall('\d*\.?\d+',file)
    ll_round = round(float(linking_len[1]),2)

    if ll_round >= LOWER_BOUND: # if above bound
        print(ll_round, "is ABOVE BOUND")
        ll.append(ll_round)
        G = nx.read_gexf(file)

        ## calculate avg clustering coefficient (c_bar) of graph
        clustering = nx.algorithms.cluster.average_clustering(G)
        c_bar.append(clustering)

np.save(str(z)+'/backup/c_bar_'+str(z), c_bar)
np.save(str(z)+'/backup/ll_cbar_'+str(z), ll)

c_bar_old = np.load(str(z)+'/graph_prop/c_bar-'+str(z)+'.npy')
ll_old = np.load(str(z)+'/graph_prop/radii_'+str(z_num)+'.npy')

pairs = np.transpose(np.array([np.concatenate([c_bar_old,c_bar]), np.concatenate([ll_old,ll])]))
sorted = pairs[pairs[:,0].argsort()]
np.save(str(z)+'/graph_prop/sorted/c_bar_'+str(z_num), sorted[:,0])
