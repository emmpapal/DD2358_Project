Second Optimization Technique: GPU
==================================
PyTorch GPU support is considered an optimization technique for HPC applications. GPUs are highly parallel processors designed to handle large volumes of data in parallel, making them well-suited for certain types of computations, such as those involved in deep learning and scientific computing. PyTorch, on the other side, is a popular open-source machine learning library that provides support for GPU acceleration. In HPC applications, the use of PyTorch with GPU support can lead to significant performance improvements, as it allows for the acceleration of computations that would otherwise take much longer to execute on a CPU-only system. In this second optimization step we modified our vectorized code using PyTorch to port it to the Nvidia GPU provided in Google's colab environment. In Figure ?, is presented part of the modified code utilizing the PyTorch library to be compatible for GPU execution.

.. contents:: Modules
   :local:
   :depth: 2

.. figure:: _static/pytorch.png
   :align: center
   :width: 50%
   :alt: Simulation code using PyTorch
   :name: fig:pytorch

   Simulation code using PyTorch

**Figure 4**: Simulation code using PyTorch.

  
