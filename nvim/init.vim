syntax on
set mouse=a
set number
set noerrorbells	
set sw=3
set expandtab
set smartindent
set number
set nowrap
set noswapfile
set ignorecase
set clipboard=unnamedplus
set encoding=utf-8
set cursorline
set termguicolors
set colorcolumn=120
set autoindent
set shiftwidth=4
set cc=80
filetype plugin indent on
highlight ColoColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/.local/share/nvim/plugged')

Plug 'yggdroot/indentline'
Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/nerdtree'

call plug#end()

let ayucolor="dark"
let g:gruvbox_contrast_dark="hard"
colorscheme gruvbox
let g:airline#extensions#tabline#enabled = 1
