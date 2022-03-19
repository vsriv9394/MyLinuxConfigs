import os
from subprocess import call

home = os.environ['HOME']


def install():

    if not os.path.exists(home + '/bin'):
        call('mkdir -p ' + home + '/bin', shell=True)
        input('Please source your rc file again... [Press any key]')
    thisdir = os.path.dirname(os.path.abspath(__file__))
    with open(home + '/bin/gitsync', 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('python ' + thisdir + '/gitsync.py $@')
    call('/bin/chmod +x ' + home + '/bin/gitsync', shell=True)


def uninstall():

    call('rm -f ' + home + '/bin/gitsync')
