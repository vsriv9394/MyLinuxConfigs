import os
from shutil import which
from subprocess import call as subp_call

home = os.environ['HOME']


# Test comment
def call(cmd): subp_call(cmd, shell=True)


def setup(localFile, configFile, createDir=False):
    localFile = os.path.abspath(localFile)
    if createDir:
        call('mkdir -p %s' % os.path.dirname(configFile))
    if os.path.exists(configFile):
        if os.path.islink(configFile):
            print('Removing existing symbolic link ' + configFile)
            call('rm ' + configFile)
        else:
            print('Creating backup for ' + configFile)
            call('mv ' + configFile + ' ' + configFile + '.bak')
    print('Creating symbolic link ' + configFile)
    call('ln -s ' + localFile + ' ' + configFile)


inp = input("Enable git to store your credentials on this machine? (y/n): ")
if inp in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print('Storing your credentials on this machine')
    with open('~/.gitconfig', 'w') as f:
        f.write('[credential "https://github.com"]\n')
        f.write('\tuseHttpPath = true\n')
        f.write('[credential]\n')
        f.write('\thelper = store\n')
print(
    'Please call "git config --global' +
    ' credential.helper erase" to erase stored credentials'
)

setup('tmux.conf', home + '/.tmux.conf')
setup('vimrc', home + '/.vimrc')
setup('inputrc', home + '/.inputrc')
setup('vim/colors', home + '/.vim/colors')
setup('vim/autoload', home + '/.vim/autoload')

if which('nvim') is not None:
    if which('npm') is None:
        inp = input('Install nodejs and npm? (y/n):')
        if inp in ['y', 'Y', 'yes', 'Yes', 'YES']:
            print(
                '--------------------------------------'
                '--------------------------------------'
            )
            call('sudo apt-get install nodejs npm')
            print(
                '--------------------------------------'
                '--------------------------------------'
            )
    if which('clangd') is None:
        inp = input('Install clangd-10? (y/n):')
        if inp in ['y', 'Y', 'yes', 'Yes', 'YES']:
            print(
                '--------------------------------------'
                '--------------------------------------'
            )
            call('sudo apt-get install clangd-10')
            call(
                'sudo update-alternatives --install '
                '/usr/bin/clangd clangd /usr/bin/clangd-10 100'
            )
            print(
                '--------------------------------------'
                '--------------------------------------'
            )
    packerFile = '/.local/share/nvim/site/pack/packer/start/packer.nvim'
    if not os.path.exists(home + packerFile):
        print(
            '--------------------------------------'
            '--------------------------------------'
        )
        print('Installing packer for neovim...')
        call(
            'git clone --depth 1 https://github.com/wbthomason/packer.nvim '
            + home + '/.local/share/nvim/site/pack/packer/start/packer.nvim'
        )
        print(
            '--------------------------------------'
            '--------------------------------------'
        )
    setup('nvim/init.lua', home + '/.config/nvim/init.lua')
    setup('nvim/lua', home + '/.config/nvim/lua')
    setup('nvim/colors', home + '/.config/nvim/colors')
    setup('nvim/autoload', home + '/.config/nvim/autoload')
    inp = input(
        'NOTE: Perform a PackerSync from inside nvim... '
        '(Press any key)'
    )
    inp = input(
        'NOTE: Run "LspInstall clangd" and "LspInstall pylsp" '
        'to install the correct language servers... (Press any key)'
    )
    inp = input(
        'NOTE: You might need to "pip install pyright" from within '
        'the python venv used during installation of nvim... '
        '(Press any key)'
    )
