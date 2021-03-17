import networkx as nx
import numpy as np
import glob

z = 'z1'
z_num = 1

## load in old files
alpha_old = np.load(str(z)+'/graph_prop/alpha_'+str(z_num)+'.npy')
clq_num_old = np.load(str(z)+'/graph_prop/clique_number_'+str(z_num)+'.npy')
max_clq_num_old = np.load(str(z)+'/graph_prop/max_clique_num_'+str(z_num)+'.npy')
s1_old = np.load(str(z)+'/graph_prop/s1_'+str(z_num)+'.npy')
s2_old = np.load(str(z)+'/graph_prop/s2_'+str(z_num)+'.npy')
tau_old = np.load(str(z)+'/graph_prop/tran_'+str(z_num)+'.npy')
ll_old = np.load(str(z)+'/graph_prop/radii_'+str(z_num)+'.npy')
print("old files loaded")

alpha = np.load(str(z)+'/backup/alpha_' + str(z)+'.npy')
clique_num = np.load(str(z)+'/backup/clique_number_' + str(z)+'.npy')
max_clique_num = np.load(str(z)+'/backup/max_clique_num_' + str(z)+'.npy')
s1 = np.load(str(z)+'/backup/s1_' + str(z)+'.npy')
s2 = np.load(str(z)+'/backup/s2_' + str(z)+'.npy')
tau = np.load(str(z)+'/backup/tran_' + str(z)+'.npy')
ll = np.load(str(z)+'/backup/radii_'+ str(z)+'.npy')
print("new files loaded")

list_old = [alpha_old, clq_num_old, max_clq_num_old, s1_old, s2_old, tau_old]
list_new = [alpha, clique_num, max_clique_num, s1, s2, tau]
names = ['alpha', 'clique_number', 'max_clique_num', 's1', 's2', 'tau']

## combine w old files & save
ll_combined = np.concatenate([ll_old,ll])
print(ll_combined.shape)
for i in range(len(list_old)):
    data = np.concatenate([list_old[i],list_new[i]])
    print(data.shape)
    pairs = np.transpose(np.array([data,ll_combined]))
    sorted = pairs[pairs[:,0].argsort()]
    np.save(str(z)+'/graph_prop/sorted/'+names[i]+'-'+str(z_num)+'.npy', sorted[:,0])
    print(names[i], 'saved at '+str(z)+'/graph_prop/sorted/'+names[i]+'-'+str(z_num)+'.npy')

np.save(str(z)+'/graph_prop/sorted/radii-'+str(z_num)+'.npy', sorted[:,1])
