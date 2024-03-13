import matplotlib.pyplot as plt
import numpy as np

from functools import wraps
from timeit import default_timer as timer

init_runtime = []

# decorator to time
def t_init(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = timer()
        result = fn(*args, **kwargs)
        t2 = timer()
        init_runtime.append(t2 - t1)
        return result
    return measure_time

"""
Create Your Own Active Matter Simulation (With Python)
Philip Mocz (2021) Princeton Univeristy, @PMocz

Simulate Viscek model for flocking birds

"""
# @timefn
# @profile
def init(Nt, N):
	""" Finite Volume simulation """

	# Simulation parameters
	v0           = 1.0      # velocity
	eta          = 0.5      # random fluctuation in angle (in radians)
	L            = 10       # size of box
	R            = 1        # interaction radius
	dt           = 0.2      # time step
	# Nt           = 200      # number of time steps
	# N            = 500      # number of birds
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
		mean_theta = theta
		for b in range(N):
			neighbors = (x-x[b])**2+(y-y[b])**2 < R**2
			sx = np.sum(np.cos(theta[neighbors]))
			sy = np.sum(np.sin(theta[neighbors]))
			mean_theta[b] = np.arctan2(sy, sx)

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
	# for i in range(50):
	init(200, 500)
	# print(f"Mean execution time of Active Matter Simulation is {sum(execTime)/len(execTime)} seconds")
	
	# Plotting
	# plt.figure()
	# plt.plot(range(1, 51), execTime, marker='o', color='b')
	# plt.xlabel('Run')
	# plt.ylabel('Execution Time (seconds)')
	# plt.title('Execution Time for Active Matter Simulation')
	# plt.show()