-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")

vim.notify = require("notify")

vim.cmd([[imap <silent><script><expr> <C-a> copilot#Accept("\<CR>")]])
