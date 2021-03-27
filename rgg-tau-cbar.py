import networkx as nx
import numpy as np
import random
import collections

def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees)

alpha = []
s1 = []
s2 = []
ll = []
max_clq_sz = []
max_clq_num = []
tau = []
cbar = []

z = 'z0' #TODO: update redshift
n = 406793 # TODO: update number of nodes

pos = {i: (random.uniform(0, 1000), random.uniform(0, 1000), random.uniform(0, 1000)) for i in range(n)}

for linking_len in np.arange(0,16,0.25): # TODO: update range

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
    s1.append(SA)

    ## calculate s2
    if len(graph_cc) > 1:
        G1 = len(G.subgraph(graph_cc[1]))
    else:
        G1 = 0
    S1 = G1/G.number_of_nodes()
    s2.append(S1)

    ## calculate max clique size
    max_clq_sz.append(nx.graph_clique_number(G))

    ## calculate # of maximal cliques
    max_clq_num.append(nx.graph_number_of_cliques(G))

    ## calculate # of maximal cliques
    tau.append(nx.algorithms.cluster.transitivity(G))

    ## calculate avg clustering coefficient (cbar) of graph
    cbar.append(nx.algorithms.cluster.average_clustering(G))

# print(ll)
# print(alpha)
# print(s1)
# print(s2)
# print(max_clq_sz)
# print(max_clq_num)
# print(tau)
# print(cbar)
np.save(str(z)+'/radii', ll)
np.save(str(z)+'/alpha', alpha)
np.save(str(z)+'/S1', s1)
np.save(str(z)+'/S2', s2)
np.save(str(z)+'/max_clq_sz', max_clq_sz)
np.save(str(z)+'/max_clq_num', max_clq_num)
np.save(str(z)+'/tau', tau)
np.save(str(z)+'/cbar', cbar)
