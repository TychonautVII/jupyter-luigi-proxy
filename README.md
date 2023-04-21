# jupyter-luigi-proxy
A basic luigi proxy for jupyter 

# Setting up for local development
You must have jupyterlab working locally, to install this package into a kernel

to setup the virtual environment, run 

pipenv install --dev

then install the kernel with

source scripts/kernel.sh 

# 

jupyter labextension install dask-labextension