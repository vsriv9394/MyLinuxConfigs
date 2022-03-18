from gitsync.install import install as install_gitsync
from INSTALL.basic import installConfig_basic
from INSTALL.nvim import installConfig_nvim
from INSTALL.shell import installConfig_shell
from INSTALL.externals import installExternals

installExternals('x86_64')

installConfig_shell()
installConfig_basic()
installConfig_nvim()

install_gitsync()
