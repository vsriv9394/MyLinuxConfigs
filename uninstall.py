from gitsync.install import uninstall as uninstall_gitsync
from INSTALL.basic import uninstallConfig_basic
from INSTALL.nvim import uninstallConfig_nvim
from INSTALL.shell import uninstallConfig_shell

uninstallConfig_shell()

uninstallConfig_basic()
uninstallConfig_nvim()

uninstall_gitsync()
