import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

positions = np.load('pos_halo.npy')

import numpy as np
from scipy import spatial
import networkx as nx
import matplotlib.pyplot as plt

def make_graph(radius):
    r = radius
    print('Making graph with radius ', r)
    kdtree = spatial.KDTree(positions)
    pairs = kdtree.query_pairs(r)
    G = nx.Graph()
    G.add_nodes_from(range(len(positions)))
    wt_edge_pairs = weighted_edge_pairs(positions,pairs)
    G.add_weighted_edges_from(wt_edge_pairs)
    nx.write_gexf(G,"graphs/halo-radius-"+str(r)+".gexf")

def weighted_edge_pairs(positions, pairs):
    uvw = []
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        dist = np.sum((positions[a] - positions[b])**2)
        uvw.append([a,b,dist])
    return uvw

R = np.arange(1,20,0.25)
for r in R:
    make_graph(r)
