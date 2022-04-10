import os
import argparse
from subprocess import call as scall
from subprocess import check_output


def call(cmd):

    scall(cmd, shell=True)


def getOutput(cmd):

    return (check_output(cmd.split())).decode()


def checkBranchName(branchName):

    if branchName[0] == '*': return branchName[1:].strip(), True
    else: return branchName.strip(), False


def getBranchInfo():
    
    currentBranch = ''
    assert os.path.exists('.git'), 'This is not a git repo'
    branchList = getOutput('git branch').split('\n')
    while '' in branchList: branchList.remove('')
    for i in range(len(branchList)):
        branchList[i], isCurrent = checkBranchName(branchList[i])
        if isCurrent: currentBranch = branchList[i]
    assert currentBranch != ''
    branchList.remove(currentBranch)
    branchList.insert(0, currentBranch)
    return currentBranch, branchList


def syncBranch(branchName):

    call('git checkout ' + branchName)
    call('git pull')
    call('git add --all')
    if getOutput('git diff-index HEAD --') != '':
        commitMsg = input('Please enter a commit msg: ')
        if commitMsg != '':
            call('git commit -m "' + commitMsg + '"')
        else:
            print('===== NOT COMMITTED =====')
    call('git push -u origin ' + branchName)


def gitsync():

    currentBranch, branchList = getBranchInfo()
    for branch in branchList: syncBranch(branch)
    call('git checkout ' + currentBranch)


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
