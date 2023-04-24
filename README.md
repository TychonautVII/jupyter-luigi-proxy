# jupyter-luigi-proxy
A basic luigi proxy for jupyter 

# Setting up for local development
You must have jupyterlab working locally, to install this package into a kernel

to setup the virtual environment, run 

pipenv install --dev

then install the kernel with

source scripts/kernel.sh 

# 
pip install jupyter-server-proxy

jupyter server extension enable jupyter_server_proxyy

jupyter labextension install @jupyterlab/server-proxy




jupyter labextension enable --sys-prefix jupyter_server_proxy

jupyter labextension uninstall @jupyterlab/server-proxy

jupyter labextension install dask-labextension

jupyter labextension list

jupyter serverextension disable --sys-prefix server-proxy

# 
jupyter labextension install @jupyterlab/jupyter-server-proxy
sudo jupyter lab build
pip install git+https://github.com/TychonautVII/jupyter-luigi-proxy.git@3205e10