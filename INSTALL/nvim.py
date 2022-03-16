import os
from .utils import backupAndAddLink, removeLinkAndRestoreBackup, call
from .utils import home, myconfigdir
from shutil import which


def runNeovimCommand(msg='', cmd=''):

    chk = input('Do you want Neovim to ' + msg + '? [y/n]: ')
    while chk not in ['y', 'Y', 'n', 'N']:
        print('Invalid input')
        chk = input('Do you want Neovim to ' + msg + '? [y/n]: ')
    if chk in ['y', 'Y']:
        call("nvim -c '" + cmd + "'")


def installConfig_nvim():

    if which('nvim') is not None:

        install_npm()
        install_clangd()
        install_packer()

        backupAndAddLink(
            src=myconfigdir + '/configs/nvim/init.lua',
            dest=home + '/.config/nvim/init.lua'
        )
        backupAndAddLink(
            src=myconfigdir + '/configs/nvim/lua',
            dest=home + '/.config/nvim/lua'
        )
        backupAndAddLink(
            src=myconfigdir + '/configs/nvim/colors',
            dest=home + '/.config/nvim/colors'
        )
        backupAndAddLink(
            src=myconfigdir + '/configs/nvim/autoload',
            dest=home + '/.config/nvim/autoload'
        )

        runNeovimCommand(
            msg='sync packages',
            cmd='PackerSync'
        )
        runNeovimCommand(
            msg='install LSP client for clangd',
            cmd='LspInstall clangd'
        )
        runNeovimCommand(
            msg='install LSP client for pylsp',
            cmd='LspInstall pylsp'
        )
        runNeovimCommand(
            msg='install LSP client for texlab',
            cmd='LspInstall texlab'
        )


def uninstallConfig_nvim():

    if which('nvim') is not None:

        removeLinkAndRestoreBackup(
            src=myconfigdir + '/configs/nvim/init.lua',
            dest=home + '/.config/nvim/init.lua'
        )
        removeLinkAndRestoreBackup(
            src=myconfigdir + '/configs/nvim/lua',
            dest=home + '/.config/nvim/lua'
        )
        removeLinkAndRestoreBackup(
            src=myconfigdir + '/configs/nvim/colors',
            dest=home + '/.config/nvim/colors'
        )
        removeLinkAndRestoreBackup(
            src=myconfigdir + '/configs/nvim/autoload',
            dest=home + '/.config/nvim/autoload'
        )


def install_npm():

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


def install_clangd():

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


def install_packer():

    packerDest = '/.local/share/nvim/site/pack/packer/start/packer.nvim'

    if not os.path.exists(home + packerDest):
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
