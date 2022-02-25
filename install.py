import os
home = os.environ['HOME']

from subprocess import call as subp_call
def call(cmd): subp_call(cmd, shell=True)

def setup(localFile, configFile):
    localFile = os.path.abspath(localFile)
    if os.path.exists(configFile):
        if os.path.islink(configFile):
            print('Removing existing symbolic link file ' + configFile)
            call('rm ' + configFile)
        else:
            print('Creating backup for ' + configFile)
            call('mv ' + configFile + ' ' + configFile + '.bak')
    call('ln -s ' + localFile + ' ' + configFile)

setup('tmux.conf', home + '/.tmux.conf')
setup('vimrc'    , home + '/.vimrc')
setup('inputrc'  , home + '/.inputrc')
