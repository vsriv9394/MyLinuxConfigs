import os
from subprocess import call as scall


home = os.environ['HOME']
myconfigdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def getConfirmation(msg):

    chk = input(msg + ' [y/n]: ')
    while chk not in ['y', 'Y', 'n', 'N']:
        print('Invalid Input...')
        chk = input(msg + ' [y/n]: ')
    return chk in ['y', 'Y']


def call(cmd):

    scall(cmd, shell=True)


def backupAndAddLink(dest=None, src=None):

    def createDestDirIfNotExists():

        call('mkdir -p ' + os.path.dirname(dest))

    def fileAlreadyExists():

        return os.path.basename(dest) in os.listdir(os.path.dirname(dest))

    def existingFileIsActiveLink():

        return os.path.islink(dest)

    def existingFileIsBrokenLink():

        return not os.path.exists(dest)

    def linkPointsToSrc():

        return os.readlink(dest) == os.path.abspath(src)

    # -------------------------------------------------------------------------

    linkingIsNeeded = True

    createDestDirIfNotExists()

    if fileAlreadyExists():

        if existingFileIsBrokenLink():

            print('Removing existing broken symbolic link ' + dest)
            call('rm ' + dest)

        elif existingFileIsActiveLink():

            if not linkPointsToSrc():

                print('Removing existing active symbolic link ' + dest)
                call('rm ' + dest)

            else:

                linkingIsNeeded = False

        else:

            print('Creating backup for file ' + dest)
            call('mv ' + dest + ' ' + dest + '.bak')

    if linkingIsNeeded:

        print('Creating symbolic link ' + dest)
        call('ln -s ' + os.path.abspath(src) + ' ' + dest)

    else:

        print('Nothing to be done... Correct link exists at ' + dest)


def removeLinkAndRestoreBackup(src=None, dest=None):

    def fileAlreadyExists():

        return os.path.basename(dest) in os.listdir(os.path.dirname(dest))

    def existingFileIsActiveLink():

        return os.path.islink(dest)

    def existingFileIsBrokenLink():

        return not os.path.exists(dest)

    def linkPointsToSrc():

        return os.readlink(dest) == os.path.abspath(src)

    # -------------------------------------------------------------------------

    deletionIsNeeded = False

    if fileAlreadyExists():

        if existingFileIsBrokenLink():

            deletionIsNeeded = True

        if existingFileIsActiveLink():

            if linkPointsToSrc():

                deletionIsNeeded = True

    if deletionIsNeeded:

        print('Deleting symbolic link ' + dest)
        call('rm ' + dest)

    if os.path.exists(dest + '.bak'):

        print('Restoring backup from file for ' + dest)
        call('mv ' + dest + '.bak' + ' ' + dest)
