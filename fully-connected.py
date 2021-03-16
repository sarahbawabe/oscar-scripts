import networkx as nx
import code.graph as g
import numpy as np

positions = np.load('0-250-pos.npy')
print("FULL POSITIONS SHAPE:", positions.shape)

graph = g.build_graph(positions, fullyConnected=True)

for node in graph.nodes:
    graph.nodes[node]['coords'] = ''
    graph.nodes[node]['color'] = ''
    graph.nodes[node]['ec'] = ''

nx.write_gexf(graph,"0-250-fc.gexf")
