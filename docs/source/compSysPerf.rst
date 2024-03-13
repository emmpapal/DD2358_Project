Computation and memory system performance
=========================================
Profiling is necessary in order to find performance bottlenecks and fix these parts of the code that are responsible for them. We could also skip the profiling and choose randomly code parts to be improved but this involves the risk of generating further problems. We might commence by profiling the code for how it is originally yet this somehow deceives the focus for optimization as most of the execution time is consumed by plotting in real time the results hence not by vectors computation. The cornerstone of the computation is working out the average angle of all the neighbours of a certain particle which will be used to update the velocity therefore this is where our focus will lay on. While exploring active matter's system performance, the execution time of the simulation code is measured for a varying number of time steps (Nt) and birds (N). Also we computed the mean runtime iterating the execution 50 times. To obtain the execution time of the code, timing decorators are defined that take the active matter function as an argument. 
We used the *line profiler* to examine the system's performance by the provided information regarding the amount of hits and the computation time of each line. 

.. contents:: Modules
   :local:
   :depth: 2
  
.. figure:: _static/init_time_runs.png
   :align: center
   :width: 70%
   :alt: Execution time of active matter for 50 iterations
   :name: fig:init_runs_1

.. figure:: _static/init_time_runs2.png
   :align: center
   :width: 70%
   :alt: Execution time of active matter for 50 iterations
   :name: f

We also used the *memory profiler* to measure memory usage of the code on a line-by-line basis. 

