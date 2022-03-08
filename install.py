import os
home = os.environ['HOME']

from subprocess import call as subp_call
def call(cmd): subp_call(cmd, shell=True)

def setup(localFile, configFile, createDir=False):
    localFile = os.path.abspath(localFile)
    if createDir:
        call('mkdir -p %s' % os.path.dirname(configFile))
    if os.path.exists(configFile):
        if os.path.islink(configFile):
            print('Removing existing symbolic link file ' + configFile)
            call('rm ' + configFile)
        else:
            print('Creating backup for ' + configFile)
            call('mv ' + configFile + ' ' + configFile + '.bak')
    call('ln -s ' + localFile + ' ' + configFile)

setup('tmux.conf' , home + '/.tmux.conf' )
setup('vimrc'     , home + '/.vimrc'     )
setup('inputrc'   , home + '/.inputrc'   )
setup('vim/colors', home + '/.vim/colors')

input = "Enable git to store your credentials on this machine? (y/n): "
if input in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print('Storing your credentials on this machine')
    call('git config --global credential.helper store')
else:
    print('No action taken for git credential.helper')
print('Please call "git config --global credential.helper erase" to erase stored credentials')
