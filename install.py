from gitsync.install import install as install_gitsync
from INSTALL.basic import installConfig_basic
from INSTALL.nvim import installConfig_nvim
from INSTALL.shell import installConfig_shell

installConfig_shell()
installConfig_basic()
installConfig_nvim()

install_gitsync()
