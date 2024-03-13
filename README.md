# DD2358_Project
## Introduction to High Performance Computing - Final Project

This repository consists of all the executable files used in our project.
The project was about optimizing the active matter simulation code that 
can be found here https://github.com/pmocz/activematter-python.
The main part of the work was executed on Google's Colab environment. 
To execute the code you have to download the IPython notebook and either 
upload the file in Google colab or run it locally on your computer in Jypyter notebook. 
However, we recommend using the first option since the code hasn't been tested 
on Jupyter and adjustments might be needed to execute parts of the code on a GPU. 

To utilize the GPU in Google Colab, the runtime type shall be changed. 
Thus, go to Runtime->Change runtime type and choose T4 GPU as Hardware accelerator. 

To execute the vectorized code that uses Cython annotations, you need the following files:
1. cy_activematter.c
2. cy_activematter.cpython-310-x86_64-linux-gnu.so
3. cy_activematter.pyx
4. cython_vec_opt.py

To execute it, open a terminal and type the following command "python3 cython_vec_opt.py". 

Finally, to see the documentation generated with Sphinx, you shall download on your PC the files of this repository.
Then navigate to the directory "DD2358_Project/docs/build/html" and double click the "index.html" file and it'll open 
a window on your browser. 


