import matplotlib.pyplot as plt
import numpy as np
import cy_activematter
import statistics

from functools import wraps
from timeit import default_timer as timer

def vectorized(Nt, N):
	""" Finite Volume simulation """

	# Simulation parameters
	v0           = 1.0      # velocity
	eta          = 0.5      # random fluctuation in angle (in radians)
	L            = 10       # size of box
	R            = 1        # interaction radius
	dt           = 0.2      # time step
	# Nt         = 200      # number of time steps
	# N          = 500      # number of birds
	plotRealTime = False

	# Initialize
	np.random.seed(17)      # set the random number generator seed

	# bird positions
	x = np.random.rand(N,1)*L
	y = np.random.rand(N,1)*L

	# bird velocities
	theta = 2 * np.pi * np.random.rand(N,1)
	vx = v0 * np.cos(theta)
	vy = v0 * np.sin(theta)

  # Prep figure
	if plotRealTime:
		fig = plt.figure(figsize=(4,4), dpi=80)
		ax = plt.gca()

	# Simulation Main Loop
	for i in range(Nt):

		# move
		x += vx*dt
		y += vy*dt

		# apply periodic BCs
		x = x % L
		y = y % L

		# find mean angle of neighbors within R
		x_diff = np.expand_dims(x, axis=1) - x
		y_diff = np.expand_dims(y, axis=1) - y
		neighbors = (x_diff**2 + y_diff**2) < R**2
		sx = np.sum(np.cos(theta) * neighbors, axis=1)
		sy = np.sum(np.sin(theta) * neighbors, axis=1)
		mean_theta = np.arctan2(sy, sx)

		# add random perturbations
		theta = mean_theta + eta*(np.random.rand(N,1)-0.5)

		# update velocities
		vx = v0 * np.cos(theta)
		vy = v0 * np.sin(theta)

		# plot in real time
		if plotRealTime:
			plt.cla()
			plt.quiver(x,y,vx,vy)
			ax.set(xlim=(0, L), ylim=(0, L))
			ax.set_aspect('equal')
			ax.get_xaxis().set_visible(False)
			ax.get_yaxis().set_visible(False)
			plt.pause(0.001)

	if plotRealTime:
		plt.savefig('activematter.png',dpi=240)
		plt.show()

	return 0

if __name__== "__main__":
	vec_runtime = []
	cy_vec_runtime = []

	# Execute for 50 iterations and compute the mean runtime
	for i in range(50):
		t1 = timer()
		vectorized(200, 500)
		t2 = timer()
		vec_runtime.append(t2-t1)
		
		t3 = timer()
		cy_activematter.main_vector() 
		t4 = timer()
		cy_vec_runtime.append(t4-t3)
	
	print(f"Mean execution of Vectorized implementation: {sum(vec_runtime)/len(vec_runtime)} seconds")
	print(f"Mean execution of Cython-Vectorized implementation: {sum(cy_vec_runtime)/len(cy_vec_runtime)} seconds")
	print()

	# Plotting
	plt.figure()
	plt.plot(range(1, 51), vec_runtime, marker='o', label='Vectorized')
	plt.plot(range(1, 51), cy_vec_runtime, marker='o', label='Cython-Vectorized')

	plt.xlabel('iteration')
	plt.ylabel('execution time (seconds)')
	plt.title('Execution Time for Active Matter Simulation')
	plt.legend()
	plt.savefig('exec_time.png')
	plt.show()