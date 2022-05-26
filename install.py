from gitsync.install import install as install_gitsync
from INSTALL.basic import installConfig_basic
from INSTALL.nvim import installConfig_nvim
from INSTALL.shell import installConfig_shell
from INSTALL.externals import installExternals

def getOption(question, validResponseList):
    question += ' (' + '/'.join(validResponseList) + ')'
    question += '[' + validResponseList[0] + '] '
    response = ''
    while response not in validResponseList:
        response = input(question)
        if response=='': response = validResponseList[0]
        if response not in validResponseList: print('Invalid Option')
        else: return response

installConfig_shell()
installConfig_basic()

neovimNeeded = getOption('Do you wish to install neovim and associated packages?', ['n', 'y'])
if neovimNeeded == 'y':
    platform = getOption('Please provide the hardware platform being used', ['x86_64', 'ppc64le'])
    installExternals(platform)
    installConfig_nvim()

install_gitsync()
