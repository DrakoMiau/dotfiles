vim.cmd("set expandtab")
vim.cmd("set tabstop=2")
vim.cmd("set softtabstop=2")
vim.cmd("set shiftwidth=2")
vim.cmd("set number")
vim.cmd("set relativenumber")
vim.cmd("set colorcolumn=81")
vim.cmd("set smartindent")
vim.cmd("set showtabline=4")
vim.g.mapleader = " "

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)



local opts = {}
require("lazy").setup("plugins")
local builtin = require("telescope.builtin")
vim.keymap.set('n', '<C-p>', builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
vim.keymap.set('n', '<leader>e', ':Neotree filesystem reveal left<CR>',{})
local config = require("nvim-treesitter.configs")

config.setup({
    ensure_installed = {"c", "lua", "cpp", "java", "javascript", "html", "css", "go", "python", "zig", "yaml", "xml", "sql", "rust", "latex", "julia", "json", "json5", "haskell", "c_sharp", "ruby", "erlang", "elixir"},
    indent = { enable = true }, 
})
    
vim.cmd("colorscheme duskfox")
