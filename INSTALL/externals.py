import os
from subprocess import call as scall


def call(cmd):

    scall(cmd, shell=True)


opd = os.path.dirname
opa = os.path.abspath
opj = os.path.join
dirname = opj(opd(opd(opa(__file__))), 'externals')

externals = {

    # Text editor
    'nvim':
    {
        'install': True,
        'x86_64': 'https://github.com/neovim/neovim/releases/'
                  'download/stable/nvim-linux64.tar.gz',
        'custom':
                  'mkdir -p ' + dirname + '/nvim;'
                  'git clone https://github.com/neovim/neovim;'
                  'cd neovim; git checkout stable;'
                  'make CMAKE_INSTALL_PREFIX=' + dirname + '/nvim;'
                  'make install -j;'
                  'cd ..; rm -rf neovim;'
    },

    # NodeJS (Contains NPM which is required for LSP)
    'node':
    {
        'install': True,
        'x86_64': 'https://nodejs.org/dist/v16.14.1/'
                  'node-v16.14.1-linux-x64.tar.xz',
        'ppc64le': 'https://nodejs.org/dist/v16.14.1/'
                   'node-v16.14.1-linux-ppc64le.tar.xz',
    },

    # LSP for C/C++
    'llvm':
    {
        'install': True,
        'x86_64': 'https://github.com/llvm/llvm-project/'
                  'releases/download/llvmorg-13.0.1/'
                  'clang+llvm-13.0.1-x86_64-linux-gnu-ubuntu-18.04.tar.xz',
        'ppc64le': 'https://github.com/llvm/llvm-project/'
                   'releases/download/llvmorg-13.0.1/'
                   'clang+llvm-13.0.1-powerpc64le-linux-rhel-7.9.tar.xz',
    },

    # LSP for Python
    'pyright':
    {
        'install': True,
        'custom': 'npm install -g pyright'
    },

    # LSP for latex
    'texlab':
    {
        'install': True,
        'x86_64': 'https://github.com/latex-lsp/texlab/releases/'
                  'download/v3.3.2/texlab-x86_64-linux.tar.gz',
        'custom': 'echo "Can install texlab only on x86_64 architectures"'
    },

}


def installBinaries(key, value):
    name = value.split('/')[-1]
    name = name.split('.')
    cmd = ''
    if name[-1] == 'gz':
        cmd = 'tar -xzf '
    if name[-1] == 'xz':
        cmd = 'tar -xf '
    ext = '.' + '.'.join(name[-2:])
    name = '.'.join(name[:-2])
    print('Installing ' + key + '...')
    call(
        'cd ' + dirname + ';'
        'wget -q ' + value + ';'
        '' + cmd + name + ext + ';'
        'rm ' + name + ext + ';'
        'mv ' + name + ' ' + key + ';'
    )


def installExternals(arch):
    call('mkdir -p ' + dirname)
    for name in externals.keys():
        if not os.path.exists(opj(dirname, name)) and \
           externals[name]['install']:
            if arch in externals[name].keys():
                installBinaries(name, externals[name][arch])
            else:
                call(externals[name]['custom'])
    with open(dirname + '/../configs/shell/paths', 'w') as f:
        f.write('export PATH="' + dirname + ':$PATH"\n')
        for name in externals.keys():
            if os.path.exists(opj(dirname, name)):
                if os.path.isdir(opj(dirname, name)):
                    f.write('export PATH="' + opj(dirname, name) +
                            '/bin:$PATH"\n')


if __name__ == '__main__':

    installExternals('x86_64')
