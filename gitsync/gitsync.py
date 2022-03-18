import os
import argparse
from subprocess import call as scall
from subprocess import check_output


def call(cmd):

    scall(cmd, shell=True)


def getOutput(cmd):

    return (check_output(cmd.split())).decode()


def syncBranch(branchName):

    assert os.path.exists('.git'), 'This is not a git repo'

    call('git checkout ' + branchName)

    call('git pull')

    if getOutput('git diff') != b'':

        commitMsg = input('Please enter a commit msg: ')

        if commitMsg != '':

            call('git add --all')
            call('git commit -m "' + commitMsg + '"')

        else:

            print(' Not committed')
    
    call('git push -u origin ' + branchName)


def gitsync():

    branchNameList = getOutput('git branch').split('\n')
    currentBranchName = 'master'
    while '' in branchNameList:
        branchNameList.remove('')
    print(branchNameList)

    for branchName in branchNameList:
        if branchName[0] == '*':
            branchName = branchName[1:].strip()
            currentBranchName = branchName
        else:
            branchName = branchName.strip()
        syncBranch(branchName)

    call('git checkout ' + currentBranchName)


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

        gitsync()
