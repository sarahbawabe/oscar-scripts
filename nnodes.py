import networkx as nx

def agrees(nnodes1, nnodes2):
    if nnodes1 == nnodes2:
        return True
    else:
        return False

print("----- COUNT # OF NODES -----")
print("\nreading z = 0")
z0_1 = nx.read_gexf('halos/10000/z0/halo-radius-6.0.gexf')
z0_2 = nx.read_gexf('halos/10000/z0/halo-radius-6.1.gexf')
if agrees(z0_1.number_of_nodes(), z0_2.number_of_nodes()):
    print("z = 0 has", z0_1.number_of_nodes(), "nodes")
else:
    print("z = 0 has disagreeing # of nodes.")

print("\nreading z = 0.5")
zp5_1 = nx.read_gexf('halos/10000/zp5/halo-radius-6.0.gexf')
zp5_2 = nx.read_gexf('halos/10000/zp5/halo-radius-6.1.gexf')
if agrees(zp5_1.number_of_nodes(),zp5_2.number_of_nodes()):
    print("z = 0.5 has", zp5_1.number_of_nodes(), "nodes")
else:
    print("z = 0.5 has disagreeing # of nodes.")

print("\nreading z = 1")
z1_1 = nx.read_gexf('halos/10000/z1/halo-radius-6.0.gexf')
z1_2 = nx.read_gexf('halos/10000/z1/halo-radius-6.1.gexf')
if agrees(z1_1.number_of_nodes(),z1_2.number_of_nodes()):
    print("z = 1 has", z1_1.number_of_nodes(), "nodes")
else:
    print("z = 1 has disagreeing # of nodes.")

print("\nreading z = 2")
z2_1 = nx.read_gexf('halos/10000/z2/halo-radius-1.0.gexf')
z2_2 = nx.read_gexf('halos/10000/z2/halo-radius-6.0.gexf')
if agrees(z2_1.number_of_nodes(),z2_2.number_of_nodes()):
    print("z = 2 has", z2_1.number_of_nodes(), "nodes")
else:
    print("z = 2 has disagreeing # of nodes.")

print("\nreading z = 3")
z3_1 = nx.read_gexf('halos/10000/z3/halo-radius-1.0.gexf')
z3_2 = nx.read_gexf('halos/10000/z3/halo-radius-6.0.gexf')
if agrees(z3_1.number_of_nodes(),z3_2.number_of_nodes()):
    print("z = 3 has", z3_1.number_of_nodes(), "nodes")
else:
    print("z = 3 has disagreeing # of nodes.")
