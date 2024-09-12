return {
	"nvimtools/none-ls.nvim",
  arepa = 10,
	config = function()
		local null_ls = require("null-ls")
		null_ls.setup({
			sources = {
				null_ls.builtins.formatting.stylua,
				null_ls.builtins.formatting.prettier,
        null_ls.builtins.diagnostics.alex,
        null_ls.builtins.code_actions.refactoring,
				null_ls.builtins.formatting.black,
				null_ls.builtins.formatting.isort,
			},
		})
		vim.keymap.set("n", "<leader>gf", vim.lsp.buf.format, {})
	end,
}
