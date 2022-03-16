import os
import sys
from subprocess import call as scall
from subprocess import check_output


def call(cmd):

    scall(cmd, shell=True)


def getOutput(cmd):

    return check_output(cmd.split())


def gitsync():

    call('git pull')

    if getOutput('git diff') != b'':

        commitMsg = input('Please enter a commit msg: ')

        if commitMsg != '':

            call('git add --all')
            call('git commit -m "' + commitMsg + '"')
            call('git push')

    else:

        print('Nothing to commit')


if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1] == 'master':

        gitdir = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)
        )))

        print('Github folder: ' + gitdir)

        # Loop over all files and directories in ~/Git
        for dir in os.listdir(gitdir):

            # Check if the current entity is a directory
            if os.path.isdir(dir):

                # Check whether the directory is a git repository
                if '.git' in os.listdir(dir):

                    os.chdir(os.path.join(gitdir, dir))
                    print('-------------------------------------'
                          '-------------------------------------')
                    print('Entering repository "' + dir + '"')
                    print('-------------------------------------'
                          '-------------------------------------')
                    gitsync()

    else:

        gitsync()
