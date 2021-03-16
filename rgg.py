import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import collections

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)

alpha = []
s_alpha = []
s1_alpha = []
ll = []
max_clq_sz = []
max_clq_num = []

n = 195748 # TODO: update number of nodes
pos = {i: (random.uniform(0, 1000), random.uniform(0, 1000), random.uniform(0, 1000)) for i in range(n)}

plt.figure(figsize=(14,7))
for linking_len in np.arange(6,30,0.1): # TODO: update range

    plt.clf() # clear the figure so that we can build a new one
    linking_len = round(linking_len,2) # round off floating point excess
    print("At ",linking_len)
    ll.append(linking_len)

    ## build a random geometric graph w that linking length
    G = nx.random_geometric_graph(n,linking_len, pos=pos)

    ## calculate & store alpha
    A = 2*G.number_of_edges()/G.number_of_nodes()
    alpha.append(A)

    ## find connected components of graph & calculate s_alpha
    graph_cc = sorted(nx.connected_components(G), key=len, reverse=True)
    G0 = len(G.subgraph(graph_cc[0])) # len of largest connected component
    SA = G0/G.number_of_nodes()
    s_alpha.append(SA)

    ## plot S1 vs ll in top left
    plt.subplot(2,2,1)
    plt.ylabel('S1')# = ' + str(SA))
    plt.xlabel('linking length [Mpc]')
    plt.plot(ll,s_alpha)
    plt.ylim([0,1])

    ## plot S2 vs ll in top right
    plt.subplot(2,2,2)
    if len(graph_cc) > 1:
        G1 = len(G.subgraph(graph_cc[1]))
    else:
        G1 = 0
    S1 = G1/G.number_of_nodes()
    s1_alpha.append(S1)
    plt.ylabel('S2')# = ' + str(S1))
    plt.xlabel('linking length [Mpc]')
    plt.plot(ll,s1_alpha)
    plt.ylim([0,0.05])

    ## plot max clique size vs ll in bottom left
    plt.subplot(2,2,3)
    max_clq_sz.append(nx.graph_clique_number(G))
    plt.ylabel('Max Clique Size')# = ' + str(S1))
    plt.xlabel('linking length [Mpc]')
    plt.plot(ll,max_clq_sz)

    ## plot # of maximal cliques vs ll in bottom right
    plt.subplot(2,2,4)
    max_clq_num.append(nx.graph_number_of_cliques(G))
    plt.ylabel('Number of Maximal Cliques')# = ' + str(S1))
    plt.xlabel('linking length [Mpc]')
    plt.plot(ll,max_clq_num)

np.save('rgg-data/z_radii', ll)
np.save('rgg-data/z_alpha', alpha)
np.save('rgg-data/z_S1', s_alpha)
np.save('rgg-data/z_S2', s1_alpha)
np.save('rgg-data/z_mcs', max_clq_sz)
np.save('rgg-data/z_mnc', max_clq_num)

plt.savefig('rgg-data/rgg.png')
