import os
import argparse
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

    parser = argparse.ArgumentParser(description='Sync options')
    parser.add_argument(
        '--all',
        default=False,
        dest='syncAllRepos',
        action='store_true'
    )

    args = parser.parse_args()

    if args.syncAllRepos:

        print('Syncing all repositories')

        gitdir = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)
        )))

        print('Github folder: ' + gitdir)

        # Loop over all files and directories in ~/Git
        for dir in os.listdir(gitdir):

            dirpath = os.path.join(gitdir, dir)

            # Check if the current entity is a directory
            if os.path.isdir(dirpath):

                # Check whether the directory is a git repository
                if '.git' in os.listdir(dirpath):

                    os.chdir(dirpath)
                    print('-------------------------------------'
                          '-------------------------------------')
                    print('Entering repository "' + dir + '"')
                    print('-------------------------------------'
                          '-------------------------------------')
                    gitsync()

                else:

                    print('"' + dir + '" is not a github repository')

            else:

                print('"' + dir + '" is not a directory')

    else:

        gitsync()
