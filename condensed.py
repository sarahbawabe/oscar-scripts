import code.kdtree as kdtree
import networkx as nx
import code.communities as comm
import numpy as np

positions = np.load('0-250-pos.npy')
radius = 20
print("radius", radius)

graph = kdtree.build_nneigh_graph(positions, radius)

print("FULL POSITIONS SHAPE:", positions.shape)

# find communities and update nodes' color attributes
communities = comm.get_communities(graph)
condensed = comm.condense_graph(communities, radius)

nx.write_gexf(condensed,"0-250-condensed-r"+str(radius)+".gexf")
