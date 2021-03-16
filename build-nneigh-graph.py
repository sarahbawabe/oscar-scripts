import code.kdtree as kdtree
import networkx as nx
import code.communities as comm
import numpy as np

# snapshot = '/gpfs/data/salexan4/Quijote-Simulations/0_fiducial/snapdir_004/snap_004'
# ids, coords = parser.read_snapshot(snapshot)

positions = np.load('sub-250-pos.npy')
radius = 20

graph = kdtree.build_nneigh_graph(positions, radius, simple=True)
nx.write_gexf(graph,"halo-full.gexf")

# print("FULL POSITIONS SHAPE:", positions.shape)

# # find communities and update nodes' color attributes
# communities = comm.get_communities(graph)
#
# condensed = comm.condense_graph(communities, radius)
#
#
# nx.write_gexf(condensed,"halo-condensed.gexf")
