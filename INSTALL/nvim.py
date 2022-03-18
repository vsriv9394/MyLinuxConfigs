import os
from .utils import backupAndAddLink, removeLinkAndRestoreBackup, call
from .utils import home, myconfigdir, getConfirmation
from shutil import which


def runNeovimCommand(msg='', cmd=''):

    if getConfirmation('Do you want neovim to ' + msg + '?'):

        call("nvim -c '" + cmd + "'")


def installConfig_nvim():

    if which('nvim') is not None:

        backupAndAddLink(
            src=myconfigdir + '/configs/nvim',
            dest=home + '/.config/nvim'
        )
        backupAndAddLink(
            src=myconfigdir + '/externals/nvim/share/nvim',
            dest=home + '/.local/share/nvim'
        )

        install_packer()

        runNeovimCommand(
            msg='sync neovim packages (Ignore any shown errors)',
            cmd='PackerSync'
        )
        runNeovimCommand(
            msg='sync vim packages',
            cmd='PlugInstall'
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
            src=myconfigdir + '/configs/nvim',
            dest=home + '/.config/nvim'
        )
        removeLinkAndRestoreBackup(
            src=myconfigdir + '/externals/nvim/share/nvim',
            dest=home + '/.local/share/nvim'
        )


def install_packer():

    #packerDest = home + '/.local/share/nvim/site/pack/packer/start/packer.nvim'
    packerDest = myconfigdir + '/externals/nvim/share/nvim/site/pack/packer/start/packer.nvim'

    if not os.path.exists(packerDest):
        print(
            '--------------------------------------'
            '--------------------------------------'
        )
        print('Installing packer for neovim...')
        call(
            'git clone --depth 1 https://github.com/wbthomason/packer.nvim '
            + packerDest
        )
        print(
            '--------------------------------------'
            '--------------------------------------'
        )
