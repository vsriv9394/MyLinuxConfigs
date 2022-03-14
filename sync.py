from getpass import getpass
from hashlib import sha256
from subprocess import call as subp_call
def call(cmd): subp_call(cmd, shell=True)


password = getpass()
if sha256(password.encode()).hexdigest()=='3f73f0428a9818bb84b11d07db9f011524b59751a163d60d9daac8f025710e71':
    call('git pull')
    call('git add --all')
    call('git commit -m "Made some changes"')
    call('git push')
else: print('Wrong password')
