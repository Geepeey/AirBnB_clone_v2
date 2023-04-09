from fabric.api import *

env.hosts = ['ubuntu@34.232.71.215', 'ubuntu@54.172.171.136']

def copy():
    put('0-setup_web_static.sh', '~/')
