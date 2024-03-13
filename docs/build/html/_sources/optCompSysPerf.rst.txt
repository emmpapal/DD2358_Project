Computation and memory system performance after optimizations
=============================================================
The optimization techniques that applied in the active matter simulation code are expected to have a positive impact on both time and memory performance. By improving the efficiency of the system, optimization techniques can reduce the time required to complete computations and minimize the amount of memory needed to store data. This leads to faster and more efficient processing of large-scale computational tasks, ultimately improving the overall performance of the system.

.. contents:: Modules
   :local:
   :depth: 2

.. figure:: _static/optimization_time_runs.png
   :align: center
   :width: 70%
   :alt: Execution time of active matter for 50 iterations using optimization techniques
   :name: fig:opt_runs_1

.. figure:: _static/optimization_time_runs2.png
    :align: center
    :width: 70%
    :alt: Execution time of active matter for 50 iterations using optimization techniques
    :name: fig:opt_runs_2

**Figure 5**: Execution time of active matter for 50 iterations using optimization techniques.

.. figure:: _static/optimization_time_steps.png
   :align: center
   :width: 42%
   :alt: Execution time of active matter for different time steps (Nt) and number of birds (N) using optimization techniques
   :name: fig:opt_steps_1

.. figure:: _static/optimization_time_birds.png
    :align: center
    :width: 42%
    :alt: Execution time of active matter for different time steps (Nt) and number of birds (N) using optimization techniques
    :name: fig:opt_steps_2

**Figure 6**: Execution time of active matter for different time steps Nt and number of birds N using optimization techniques.

From Figure 5, it is clear that using optimization techniques for a high computational problem, like the active matter, can reduce significantly the mean execution time up to 6 times for the vectorization case and up to 40 times using the PyTorch library that GPU offers. The reason why vectorization optimization techniques present worse results than GPU PyTorch is because vectorization techniques typically rely on SIMD (Single Instruction, Multiple Data) instructions, which can only parallelize a limited number of operations. GPU PyTorch, on the other hand, can leverage thousands of CUDA cores in parallel, providing much greater parallelism. Also, GPUs have much higher memory bandwidth compared to CPUs, allowing them to access and process data much faster. Vectorization techniques may not be able to fully utilize the available memory bandwidth, leading to lower performance.
It can be interesting now to run the codes with the real-time visualization of the flock of birds. After line-profiling both the non-optimized and the vectorization-optimized code, here are the obtained results:

.. figure:: _static/line_profiler_without_opt.png
   :align: center
   :width: 90%
   :alt: Line profiler on native code
   :name: fig:line_profiler_native_code

**Figure 7**: Line profiler on native code.

.. figure:: _static/line_profiler_w_opt.png
   :align: center
   :width: 90%
   :alt: Line profiler on vectorization-optimized code
   :name: fig:line_profiler_vectorized_code

**Figure 8**: Line profiler on vectorization-optimized code.

From the figures above, we can infer that the overall impact of computing the new angles becomes less significant when enhancing the code. From an overall percentage of around 12%, it drops down to 3.5% reaching a speed-up of a factor of 3.5x. Therefore, by optimizing the code, almost all the effort will be spent on projecting the active matter in real time.
