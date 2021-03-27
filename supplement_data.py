import networkx as nx
import numpy as np
import glob
import matplotlib.pyplot as plt
import re

LOWER_BOUND = 16
UPPER_BOUND = 26
z = 'z1'
z_num = 1

graph_file_list = glob.glob(str(z)+'/*.gexf')
num_files = len(graph_file_list)
print(num_files, "files read")

ll = []
alpha = []
s1 = []
s2 = []
tau = []
clique_num = []
max_clique_num = []
c_bar = []

for file in graph_file_list:

    ## extract linking len from file name
    linking_len = re.findall('\d*\.?\d+',file)
    ll_round = round(float(linking_len[1]),2)

    if ll_round >= LOWER_BOUND and ll_round < UPPER_BOUND: # if in bounds
        print(ll_round, "is IN BOUNDS")
        ll.append(ll_round)
        G = nx.read_gexf(file)

        ## calculate transitivity (tau) of graph
        transitivity = nx.algorithms.cluster.transitivity(G)
        tau.append(transitivity)

        ## calculate & store alpha
        A = 2*G.number_of_edges()/G.number_of_nodes()
        alpha.append(A)

        ## calculate alpha for s1
        graph_cc = sorted(nx.connected_components(G), key=len, reverse=True)
        G0 = len(G.subgraph(graph_cc[0])) # len of largest connected component
        SA = G0/G.number_of_nodes()
        s1.append(SA)

        ## calculate alpha for s2
        if len(graph_cc) > 1:
            G1 = len(G.subgraph(graph_cc[1]))
        else:
            G1 = 0
        S1 = G1/G.number_of_nodes()
        s2.append(S1)

        ## get max clique size
        clique_num.append(nx.graph_clique_number(G))

        ## get # of maximal cliques
        max_clique_num.append(nx.graph_number_of_cliques(G))

        ## calculate avg clustering coefficient (c_bar) of graph
        clustering = nx.algorithms.cluster.average_clustering(G)
        c_bar.append(clustering)

np.save(str(z)+'/backup2/radii_'+ str(z),ll)
np.save(str(z)+'/backup2/alpha_' + str(z),alpha)
np.save(str(z)+'/backup2/s1_'+ str(z),s1)
np.save(str(z)+'/backup2/s2_'+ str(z),s2)
np.save(str(z)+'/backup2/tran_'+ str(z),tau)
np.save(str(z)+'/backup2/clique_number_'+ str(z),clique_num)
np.save(str(z)+'/backup2/max_clique_num_'+ str(z),max_clique_num)
np.save(str(z)+'/backup2/c_bar_'+ str(z),c_bar)

# ## load in old files
# alpha_old = np.load(str(z)+'/graph_prop/alpha_'+str(z_num)+'.npy')
# c_bar_old = np.load(str(z)+'/graph_prop/c_bar-'+str(z)+'.npy')
# clq_num_old = np.load(str(z)+'/graph_prop/clique_number_'+str(z_num)+'.npy')
# max_clq_num_old = np.load(str(z)+'/graph_prop/max_clique_num_'+str(z_num)+'.npy')
# s1_old = np.load(str(z)+'/graph_prop/s1_'+str(z_num)+'.npy')
# s2_old = np.load(str(z)+'/graph_prop/s2_'+str(z_num)+'.npy')
# tau_old = np.load(str(z)+'/graph_prop/tran_'+str(z_num)+'.npy')
# ll_old = np.load(str(z)+'/graph_prop/radii_'+str(z_num)+'.npy')
#
# list_old = [alpha_old, c_bar_old, clq_num_old, max_clq_num_old, s1_old, s2_old, tau_old]
# list_new = [alpha, c_bar, clique_num, max_clique_num, s1, s2, tau]
# names = ['alpha', 'c_bar', 'clique_number', 'max_clique_num', 's1', 's2', 'tau']
#
# ## combine w old files & save
# for i in range(len(list_old)):
#     pairs = np.transpose(np.array([np.concatenate([list_old[i],list_new[i]]), np.concatenate([ll_old,ll])]))
#     sorted = pairs[pairs[:,0].argsort()]
#     np.save(str(z)+'/graph_prop/sorted/'+names[i]+'-'+str(z_num)+'.npy', sorted[:,0])

# np.save(str(z)+'/graph_prop/sorted/radii-'+str(z_num)+'.npy', sorted[:,1])

# np.save('graph_prop/alpha_' + str(z),alpha)
# np.save('graph_prop/s1_'+ str(z),S1)
# np.save('graph_prop/s2_'+ str(z),S2)
# np.save('graph_prop/radii_'+ str(z),l)
# np.save('graph_prop/tran_'+ str(z),tran)
# np.save('graph_prop/clique_number_'+ str(z),clique_number)
# np.save('graph_prop/max_clique_num_'+ str(z),max_clique_num)

# np.save(str(z)+'/graph_prop/tau-'+str(z), tau)
# np.save(str(z)+'/graph_prop/c_bar-'+str(z), c_bar)
# np.save(str(z)+'/graph_prop/ll_file-order-'+str(z), ll)
# plt.savefig(str(z)+'/graph_prop/tau-cbar-'+str(z)+'.png')
