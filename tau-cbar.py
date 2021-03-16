import networkx as nx
import numpy as np
import glob
import matplotlib.pyplot as plt
import re

z = 'z3'
graph_file_list = glob.glob(str(z)+'/*.gexf')

tau = []
c_bar = []
ll = []

num_files = len(graph_file_list)
i = 0
plt.figure(figsize=(14,5))
for file in graph_file_list:
    print(i, '/', num_files)
    plt.clf() # clear the figure so that we can build a new one
    G = nx.read_gexf(file)

    ## extract linking len from file name
    linking_len = re.findall('\d*\.?\d+',file)
    ll_round = round(float(linking_len[1]),2)
    ll.append(ll_round)

    ## calculate transitivity (tau) of graph
    transitivity = nx.algorithms.cluster.transitivity(G)
    tau.append(transitivity)

    ## plot tau vs ll in top left
    plt.subplot(1,2,1)
    plt.ylabel('Transitivity (tau)')# = ' + str(SA))
    plt.xlabel('linking length [Mpc]')
    plt.plot(ll,tau)

    ## calculate avg clustering coefficient (c_bar) of graph
    clustering = nx.algorithms.cluster.average_clustering(G)
    c_bar.append(clustering)

    ## plot c_bar vs ll in top left
    plt.subplot(1,2,2)
    plt.ylabel('Clustering Coefficient (c_bar)')# = ' + str(SA))
    plt.xlabel('linking length [Mpc]')
    plt.plot(ll,c_bar)
    i += 1

np.save(str(z)+'/graph_prop/tau-'+str(z), tau)
np.save(str(z)+'/graph_prop/c_bar-'+str(z), c_bar)
np.save(str(z)+'/graph_prop/ll_file-order-'+str(z), ll)
plt.savefig(str(z)+'/graph_prop/tau-cbar-'+str(z)+'.png')
