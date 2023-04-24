import setuptools

setuptools.setup(
    name="jupyter-jupyter-luigi-proxy",
    version='1.0dev',
    url="https://github.com/jupyterhub/jupyter-server-proxy/tree/HEAD/contrib/jupyter-luigi",
    author="Peter Mariani",
    description="peterbmariani@gmail.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'jupyter-luigi = jupyter_luigi_proxy:setup_jupyter_luigi',
        ]
    },
    package_data={
        'jupyter_jupyter_luigi_proxy': ['icons/*'],
    },
)
