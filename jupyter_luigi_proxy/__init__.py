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
        },
        "port":8082,
        "command":[
            "luigid",
            "--port",
            "{port}"
        ]
            
        
    }

if __name__ == "__main__":
    print("hello")