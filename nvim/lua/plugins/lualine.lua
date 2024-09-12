return {
	"nvim-lualine/lualine.nvim",
	dependencies = { "nvim-tree/nvim-web-devicons" },
	config = function()
		require("lualine").setup({
			options = {
				theme = "seoul256",
				component_separators = { left = "", right = "" },
				section_separators = { left = "", right = "" },
				-- '' '' '' ''
				disabled_filetypes = {
					statusline = {
						"neo-tree",
            "alpha",
					},
					winbar = {
						"neo-tree",
            "alpha"
					},
				},
				winbar = {
					lualine_a = {},
					lualine_b = {},
					lualine_c = {},
					lualine_x = {},
					lualine_y = {
						{
							"filename",
							separator = { left = " ", right = " " },
						},
					},
					lualine_z = {},
				},
				inactive_winbar = {
					lualine_a = {
						{
							"filename",
							separator = { left = " ", right = " " },
						},
					},
					lualine_b = {},
					lualine_c = {},
					lualine_x = {
						"location",
						separator = { left = " ", right = " " },
					},
					lualine_y = {},
					lualine_z = {},
				},
				extensions = { 'neo-tree' },
			},
		})
	end,
}
