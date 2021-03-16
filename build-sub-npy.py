import numpy as np


# update these parameters as necessary!
MIN = 0 # greater than or equal to
MAX = 250 # less than

positions = np.load('halos/10k/pos_halo.npy')
print("FULL POSITIONS SHAPE:", positions.shape)

pos = positions[np.all(np.where(positions < MAX, True, False), axis=1)]
print("<250 POSITIONS SHAPE:", pos.shape)

np.save("sub-250-pos.npy", pos)
