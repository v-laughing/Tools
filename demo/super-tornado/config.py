#coding=utf-8

import os
import logging
import configparser



__APP_NAME__ = 'super_demo'


sp_log_dir = '/var/log/supervisor'
sp_conf_dir = '/etc/supervisor/conf.d'


BaseSupervisorConf = {
    'program': {
        'user': 'root',
        'autorestart': 'true',
        'redirect_stderr': 'true',
        'loglevel': 'info'
    }
}

def make_supervisor_conf_file(project_path, appname, post, numprocs):
    
    ## 目录确保
    paths_need = [ sp_log_dir, sp_conf_dir ]
    for path in paths_need:
        if not os.path.exists(path):
            os.makedirs(path)
    ## 主配置文件确保
    if not os.path.exists('/etc/supervisord.conf'):
        logging.info('****** ERROR: supervisord.conf not exist! ******')
                
    supervisor_conf = configparser.ConfigParser()

    programs = ','.join(['{}-{}'.format(appname, i) for i in range(numprocs)])
    supervisor_conf['group:{}s'.format(appname)] = {
        'programs': programs
    }
    for i in range(numprocs):
        supervisor_conf['program:{}-{}'.format(appname, i)] = {
            'command': 'python3 {}/main.py --port={}'.format(project_path, post+i),
            'stdout_logfile': '{}/{}{}.log'.format(sp_log_dir, appname, i)
        }
        supervisor_conf['program:{}-{}'.format(appname, i)].update(BaseSupervisorConf['program'])
    
    with open('{}/{}.conf'.format(sp_conf_dir, appname), 'w') as conf_file:
        supervisor_conf.write(conf_file)



if __name__ == "__main__":
    make_supervisor_conf_file( os.getcwd(), __APP_NAME__, 9001, 4)
    