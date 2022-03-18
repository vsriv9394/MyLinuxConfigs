import os
from .utils import call, backupAndAddLink, removeLinkAndRestoreBackup
from .utils import home, myconfigdir


def configureGitToStorePassword():

    inp = input('Enable git to store your credentials '
                'on this machine? (y/n): ')

    while inp not in ['y', 'Y', 'n', 'N']:

        print('Invalid input')
        inp = input('Enable git to store your credentials '
                    'on this machine? (y/n): ')

    if inp in ['y', 'Y']:

        print('Storing your credentials on this machine')

        backupAndAddLink(
            src=myconfigdir + '/configs/git/gitconfig',
            dest=home + '/.gitconfig'
        )


def addPluggedPathToVimRc():

    vimfile = myconfigdir + '/configs/vim/vimrc'
    plugPath = myconfigdir + '/externals/nvim/share/nvim/plugged'
    oldFile = open(vimfile, 'r').readlines()
    with open(vimfile, 'w') as f:
        for line in oldFile:
            if line[:16] == 'call plug#begin(':
                line = 'call plug#begin(\'' + plugPath + '\')\n'
            f.write(line)


def installConfig_basic():

    configureGitToStorePassword()

    addPluggedPathToVimRc()

    backupAndAddLink(
        src=myconfigdir + '/configs/tmux/tmux.conf',
        dest=home + '/.tmux.conf'
    )

    backupAndAddLink(
        src=myconfigdir + '/configs/vim/vimrc',
        dest=home + '/.vimrc'
    )

    backupAndAddLink(
        src=myconfigdir + '/configs/readline/inputrc',
        dest=home + '/.inputrc'
    )

    backupAndAddLink(
        src=myconfigdir + '/configs/vim',
        dest=home + '/.vim'
    )


def uninstallConfig_basic():

    if os.path.islink(home + '/.gitconfig'):
        if os.readlink(home + '/.gitconfig') == myconfigdir + '/configs/git/gitconfig':
            call('rm ' + home + '/.git-credentials')

    removeLinkAndRestoreBackup(
        src=myconfigdir + '/configs/git/gitconfig',
        dest=home + '/.gitconfig'
    )

    removeLinkAndRestoreBackup(
        src=myconfigdir + '/configs/tmux/tmux.conf',
        dest=home + '/.tmux.conf'
    )

    removeLinkAndRestoreBackup(
        src=myconfigdir + '/configs/vim/vimrc',
        dest=home + '/.vimrc'
    )

    removeLinkAndRestoreBackup(
        src=myconfigdir + '/configs/readline/inputrc',
        dest=home + '/.inputrc'
    )

    removeLinkAndRestoreBackup(
        src=myconfigdir + '/configs/vim',
        dest=home + '/.vim'
    )
