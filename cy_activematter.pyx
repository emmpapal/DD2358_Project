import numpy as np
cimport numpy as cnp

def main_vector():
    """ Finite Volume simulation """
    
    # Simulation parameters
    cdef double v0 = 1.0      # velocity
    cdef double eta = 0.5     # random fluctuation in angle (in radians)
    cdef double L = 10        # size of box
    cdef double R = 1         # interaction radius
    cdef double dt = 0.2      # time step
    cdef int Nt = 200          # number of time steps
    cdef int N = 500           # number of birds
    cdef int plotRealTime = 0

    # Initialize
    np.random.seed(17)  # set the random number generator seed

    # bird positions
    cdef cnp.ndarray[cnp.double_t, ndim=2] x = np.empty((N, 1), dtype=np.double)
    cdef cnp.ndarray[cnp.double_t, ndim=2] y = np.empty((N, 1), dtype=np.double)

    # bird velocities
    cdef cnp.ndarray[cnp.double_t, ndim=2] theta = 2 * np.pi * np.random.rand(N, 1)
    cdef cnp.ndarray[cnp.double_t, ndim=2] vx = v0 * np.cos(theta)
    cdef cnp.ndarray[cnp.double_t, ndim=2] vy = v0 * np.sin(theta)

    # Simulation Main Loop
    for i in range(Nt):

        # move
        x += vx * dt
        y += vy * dt

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
        theta = mean_theta + eta * (np.random.rand(N, 1) - 0.5)

        # update velocities
        vx = v0 * np.cos(theta)
        vy = v0 * np.sin(theta)

    return 0
