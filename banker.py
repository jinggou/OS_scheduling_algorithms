#!/usr/local/bin/python3

import numpy as np

# For testing:
"""
n_processes = 5
n_resources = 3
current_available_resources = [3,3,2]
currently_allocated = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]])
max_demand = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]])
"""

# 5a i
"""
n_processes = 6
n_resources = 4
current_available_resources = np.array([1,1,2,1])
currently_allocated = np.array([[2,1,3,0],[2,0,0,1],[1,1,2,2],[1,1,0,0],[0,0,1,0],[0,1,0,2]])
max_demand = np.array([[5,3,3,2],[3,3,1,3],[4,3,4,2],[2,1,2,1],[1,0,1,1],[1,2,3,3]])
running = np.ones(n_processes) # An array with n_processes 1's to indicate if process is yet to run
"""

# 5b i
n_processes = 6
n_resources = 4
current_available_resources = np.array([0,0,0,1])
currently_allocated = np.array([[0,1,0,0],[1,0,1,1],[2,1,2,0],[1,1,2,1],[2,1,0,0],[2,0,1,1]])
max_demand = np.array([[0,1,2,1],[0,3,3,2],[0,0,0,1],[3,2,3,2],[3,0,5,1],[2,1,1,0]]) + currently_allocated
running = np.ones(n_processes) # An array with n_processes 1's to indicate if process is yet to run

while np.count_nonzero(running) > 0:
	at_least_one_allocated = False
	for p in range(n_processes):
		if running[p]:
			if all(i >= 0 for i in current_available_resources - (max_demand[p] - currently_allocated[p])):
				at_least_one_allocated = True
				print("Process " + str(p) + ": ",end="")
				print("Need --> " + str(max_demand[p] - currently_allocated[p]) + " <= " + str(current_available_resources) + " <-- Work",end="")
				print(", Allocated: " + str(currently_allocated[p]))
				running[p] = 0
				current_available_resources += currently_allocated[p]
	if not at_least_one_allocated:
		print('Unsafe')
		exit()
				
print('Safe')