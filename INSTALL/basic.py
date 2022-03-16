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


def installConfig_basic():

    configureGitToStorePassword()

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
        src=myconfigdir + '/configs/vim/colors',
        dest=home + '/.vim/colors'
    )

    backupAndAddLink(
        src=myconfigdir + '/configs/vim/autoload',
        dest=home + '/.vim/autoload'
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
        src=myconfigdir + '/configs/vim/colors',
        dest=home + '/.vim/colors'
    )

    removeLinkAndRestoreBackup(
        src=myconfigdir + '/configs/vim/autoload',
        dest=home + '/.vim/autoload'
    )
