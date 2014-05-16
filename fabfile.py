import os
from fabric.api import env, cd, run, sudo

env.forward_agent = True
env.user = "medjellydata"
env.hosts = ['morenaza.science-o-matic.com']
env.home_root = '/home/medjellydata/'
env.virtualenv_root = os.path.join(env.home_root, '.virtualenvs/medjellydata-jellyfishes-api')
env.project = {
    'name': 'medjellydata_jellyfishes_api',
    'root': os.path.join(env.home_root, 'www/medjellydata-jellyfishes-api/'),
    'pip': os.path.join(env.virtualenv_root, 'bin/pip'),
}

def _git_update(branch):
    with cd(env.project['root']):
        run('git fetch --all')
        run('git checkout %s' % branch)
        run('git reset --hard origin/%s' % branch)

def reloadapp():
    sudo('supervisorctl restart %s' % env.project['name'], shell=False)

def release(run_migrate=True, static=True, branch='master'):
    _git_update(branch)
    run('%s install -r %spip-requirements.txt' %
        (env.project['pip'], env.project['root']))
    reloadapp()
