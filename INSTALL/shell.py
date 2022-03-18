import os
from .utils import call, home

dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
localpath = os.path.join(dirpath, 'configs/shell')


def readSource(shellSource):
    '''Returns contents of the rc file as a list of lines'''
    return open(shellSource, 'r').readlines()


def deleteExistingBlock(contents):
    '''Remove block from contents'''
    beg = 0
    for iLine in range(len(contents)):
        if contents[iLine] == '# MyLinuxConfigs >>>\n':
            beg = iLine
        if contents[iLine] == '# MyLinuxConfigs <<<\n':
            del contents[beg:iLine+1]
            break
    return contents


def createNewBlock(contents):
    '''Add a new block at the end of contents'''
    contents.append('# MyLinuxConfigs >>>\n')
    contents.append('source ' + localpath + '/aliases\n')
    contents.append('source ' + localpath + '/paths\n')
    contents.append('source ' + localpath + '/shellrc\n')
    contents.append('# MyLinuxConfigs <<<\n')
    return contents


def writeSource(shellSource, contents):
    '''Overwrite contents in the bashrc'''
    open(shellSource, 'w').write(''.join(contents))


def installConfig_shell():

    shellSource = input('Enter the shellrc file being used '
                        '(default is "~/.bashrc"): ')

    if shellSource == '':
        shellSource = os.path.join(home, '.bashrc')

    open('.shellpath', 'w').write(shellSource)
    contents = readSource(shellSource)
    contents = deleteExistingBlock(contents)
    contents = createNewBlock(contents)
    writeSource(shellSource, contents)


def uninstallConfig_shell():

    shellSource = open('.shellpath', 'r').read()
    contents = readSource(shellSource)
    contents = deleteExistingBlock(contents)
    writeSource(shellSource, contents)
    call('rm .shellpath')
