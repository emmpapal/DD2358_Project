First Optimization Technique: Vectorization
===========================================
Vectorization is a key optimization technique in high-performance computing (HPC) and other areas of computing, which allow the simultaneous processing of multiple data elements. This contrasts with scalar operations, which process one data element at a time. In modern processors, vectorization is often implemented using SIMD (Single Instruction, Multiple Data) instructions. These instructions allow a single instruction to be applied to multiple data elements in parallel, greatly improving performance. In Figure 1, the initial part of the simulation code and the vectorized version are presented. 


.. contents:: Modules
   :local:
   :depth: 2

.. figure:: _static/init_code.png
   :align: center
   :width: 45%
   :alt: Initial Part of the Simulation Code
   :name: fig:init_code

   Initial Part of the Simulation Code

.. figure:: _static/vectorized_code.png
   :align: center
   :width: 45%
   :alt: Vectorized Version of the Code
   :name: fig:vectorized_code

   Vectorized Version of the Code

**Figure 1**: Comparing vectorized and unvectorized parts of the code.

The initial part of the code uses explicit loops to re-evaluate the distance between each bird from its neighbor and their new direction in the area. In the optimized version, we leverage NumPy's array operation to unroll the loop and compute the mean angle and find neighbors efficiently. In that way, the vectorized part broadcasts the *x* and *y* arrays to make them compatible to include all the birds and calculate the differences between all pairs of elements.

.. figure:: _static/perf_init_v2.png
   :align: center
   :width: 90%
   :alt: Perf tools on native code
   :name: fig:perf_native_code

.. figure:: _static/perf_vec2.png
   :align: center
   :width: 90%
   :alt: Perf tools on vectorized code
   :name: fig:perf_vectorized_code

**Figure 2**: Perf tools on native code.

**Figure 3**: Perf tools on vectorized code.

  
