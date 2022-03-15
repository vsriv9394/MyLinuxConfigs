from subprocess import call as subp_call


def call(cmd):
    subp_call(cmd, shell=True)


if __name__ == '__main__':

    msg = input('Please enter a commit message: ')
    call('git pull')
    call('git add --all')
    call('git commit -m "' + msg + '"')
    call('git push')
