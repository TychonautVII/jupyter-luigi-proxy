"""
Return config on servers to start for jupyter-luigi

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os


def setup_jupyter_luigi():
    return {
        'command': [],
        'environment': {},
        'launcher_entry': {
            'title': 'jupyter-luigi',
        }
    }

if __name__ == "__main__":
    print("hello")