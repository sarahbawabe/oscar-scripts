import code.kdtree as kdtree
import code.parser as parser
import networkx as nx
import numpy as np

# update these parameters as necessary!
MIN = 250 # greater than or equal to
MAX = 500 # less than

## READ SNAPSHOT
snapshot = '/gpfs/data/salexan4/Quijote-Simulations/0_fiducial/snapdir_004/snap_004'
ids, coords = parser.read_snapshot(snapshot)
positions = np.array(coords)/1e3 # convert to Mpc/h
print("FULL POSITIONS SHAPE:", positions.shape)

## ONLY SAVE POSITIONS WITHIN BOUNDS
pos = positions[np.all(np.where((MAX - positions) > MIN, True, False), axis=1)]
print("POSITIONS SHAPE:", pos.shape)

filename1 = str(MIN) + "-" + str(MAX) + "-pos.npy"
np.save(filename1, pos)

## BUILD GRAPH W RADIUS SEARCH
radius = 20
graph = kdtree.build_nneigh_graph(positions, radius, simple=True)

filename2 = str(MIN) + "-" + str(MAX) + "-halo-full.gexf"
nx.write_gexf(graph, filename2)
