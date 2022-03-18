import os
from .utils import backupAndAddLink, removeLinkAndRestoreBackup, call
from .utils import home, myconfigdir, getConfirmation
from shutil import which


def runNeovimCommand(msg='', cmd=''):

    if getConfirmation('Do you want neovim to ' + msg + '?'):

        call("nvim -c '" + cmd + "'")


def installConfig_nvim():

    if which('nvim') is not None:

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
