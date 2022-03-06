" Change the leader key to comma
let mapleader = " "

" Alias for the escape character (Press 'vv' to exit the visual mode)
inoremap jk <Esc>

" Set incremental search
set incsearch
set hlsearch
map <leader>h :noh<CR>

" Set line numbers
set nu

" Follow syntax
syntax on

" Colorscheme
colo onedark
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif

" Highlight the current line
set cursorline
hi clear CursorLine
hi clear CursorLineNR
hi CursorLine ctermbg=234
hi CursorLineNR ctermfg=red

" Highlight column limit of 100
set colorcolumn=100
hi ColorColumn ctermbg=234

" Do not split words while wrapping
set linebreak

" Automatic smart indentation when newline inserted
set smartindent 

" Add matching brackets, braces and parantheses
" inoremap [ []<Esc>i
" inoremap { {}<Esc>i
" inoremap ( ()<Esc>i

" Tab character details
set tabstop=4 shiftwidth=4 softtabstop=4 expandtab

" Open file where last left
if has("autocmd")
au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
\| exe "normal! g'\"" | endif
endif

" Status line ======================================================================================================
au InsertEnter * hi statusline guifg=black guibg=#d7afff ctermfg=black ctermbg=magenta
au InsertLeave * hi statusline guifg=black guibg=#8fbfdc ctermfg=black ctermbg=cyan
hi statusline guifg=black guibg=#8fbfdc ctermfg=black ctermbg=cyan
let g:currentmode={
    \ "n"      : 'Normal'   , "no"     : 'Normal·Operator Pending',
    \ "v"      : 'Visual'   , "V"      : 'V·Line'                 ,
    \ "\<C-V>" : 'V·Block'  , "s"      : 'Select'                 ,
    \ "S"      : 'S·Line'   , "\<C-S>" : 'S·Block'                ,
    \ "i"      : 'Insert'   , "R"      : 'Replace'                ,
    \ "Rv"     : 'V·Replace', "c"      : 'Command'                ,
    \ "cv"     : 'Vim Ex'   , "ce"     : 'Ex'                     ,
    \ "r"      : 'Prompt'   , "rm"     : 'More'                   ,
    \ "r?"     : 'Confirm'  , "!"      : 'Shell'                  ,
    \ "t"      : 'Terminal'
    \}
set laststatus=2
set statusline=
set statusline+=%0*\ %n\                                 " Buffer number
set statusline+=%1*\ %<%F%m%r%h%w\                       " File path, modified, readonly, helpfile, preview
set statusline+=%3*│                                     " Separator
set statusline+=%2*\ %Y\                                 " FileType
set statusline+=%3*│                                     " Separator
set statusline+=%2*\ %{''.(&fenc!=''?&fenc:&enc).''}     " Encoding
set statusline+=\ (%{&ff})                               " FileFormat (dos/unix..)
set statusline+=%=                                       " Right Side
set statusline+=%2*\ col:\ %02v\                         " Colomn number
set statusline+=%3*│                                     " Separator
set statusline+=%1*\ ln:\ %02l/%L\ (%3p%%)\              " Line number / total lines, percentage of document
set statusline+=%0*\ %{toupper(g:currentmode[mode()])}\  " The current mode
hi User1 ctermfg=007 ctermbg=239 guibg=#4e4e4e guifg=#adadad
hi User2 ctermfg=007 ctermbg=236 guibg=#303030 guifg=#adadad
hi User3 ctermfg=236 ctermbg=236 guibg=#303030 guifg=#303030
hi User4 ctermfg=239 ctermbg=239 guibg=#4e4e4e guifg=#4e4e4e
"====================================================================================================================
