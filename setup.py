import setuptools

setuptools.setup(
  name="jupyter-luigi-proxy",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['main'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'luigi = main:main',
      ]
  },
  install_requires=['jupyter-server-proxy>=3.2.2'],
  package_data={
        'jupyter_luigi_proxy': ['icons/luigi.png'],
    },
)