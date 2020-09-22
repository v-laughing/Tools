#coding=utf-8

import os
from fabric.api import local, cd

remote_project_dir = '/test/super_demo'



def deploy():
    '''pip install and start supervisor
    '''
    with cd(remote_project_dir):
        local('chmod 777 install.sh')
        local('./install.sh')

def status():
    with cd(remote_project_dir):
        local('venv/bin/supervisorctl status')
    
## some problem, no use
# def restart():
#     '''reload conf file and restart supervisor
#     '''
#     with cd(remote_project_dir):
#         local('python config.py')
#         local('venv/bin/supervisorctl update all')