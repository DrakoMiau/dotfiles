return {
  {
    "hrsh7th/cmp-nvim-lsp",
  },
  {
    "L3MON4D3/LuaSnip",
    dependencies = {
      "saadparwaiz1/cmp_luasnip",
      "rafamadriz/friendly-snippets",
    },
  },
  {
    "hrsh7th/nvim-cmp",
    dependencies = {
      "roobert/tailwindcss-colorizer-cmp.nvim",
      "onsails/lspkind.nvim",
    },
    config = function()
      local cmp = require("cmp")
      local colorizer = require("tailwindcss-colorizer-cmp")
      local lspkind = require("lspkind")
      require("luasnip.loaders.from_vscode").lazy_load()

      colorizer.setup({})

      cmp.setup({
        snippet = {
          -- REQUIRED - you must specify a snippet engine
          expand = function(args)
            require("luasnip").lsp_expand(args.body) -- For `luasnip` users.
          end,
        },
        window = {
          completion = {
            cmp.config.window.bordered(),
            col_offset = -3, -- align the abbr and word on cursor (due to fields order below)
          },
          documentation = cmp.config.window.bordered(),
        },
        formatting = {
          fields = { "kind", "abbr", "menu" },
          format = lspkind.cmp_format({
            mode = "symbol_text", -- options: 'text', 'text_symbol', 'symbol_text', 'symbol'
            maxwidth = 50,  -- prevent the popup from showing more than provided characters (e.g 50 will not show more than 50 characters)
            menu = {        -- showing type in menu
              nvim_lsp = "[LSP]",
              path = "[Path]",
              buffer = "[Buffer]",
              luasnip = "[LuaSnip]",
            },
            before = function(entry, vim_item) -- for tailwind css autocomplete
              if vim_item.kind == "Color" and entry.completion_item.documentation then
                local _, _, r, g, b =
                    string.find(entry.completion_item.documentation, "^rgb%((%d+), (%d+), (%d+)")
                if r then
                  local color = string.format("%02x", r)
                      .. string.format("%02x", g)
                      .. string.format("%02x", b)
                  local group = "Tw_" .. color
                  if vim.fn.hlID(group) < 1 then
                    vim.api.nvim_set_hl(0, group, { fg = "#" .. color })
                  end
                  vim_item.kind = "⬤" -- "■" or anything
                  vim_item.kind_hl_group = group
                  return vim_item
                end
              end
              -- vim_item.kind = icons[vim_item.kind] and (icons[vim_item.kind] .. vim_item.kind) or vim_item.kind
              -- or just show the icon
              vim_item.kind = lspkind.symbolic(vim_item.kind) and lspkind.symbolic(vim_item.kind)
                  or vim_item.kind
              return vim_item
            end,
          }),
        },

        mapping = cmp.mapping.preset.insert({
          ["<C-k>"] = cmp.mapping.select_prev_item(),
          ["<C-j>"] = cmp.mapping.select_next_item(),
          ["<C-b>"] = cmp.mapping.scroll_docs(-4),
          ["<C-f>"] = cmp.mapping.scroll_docs(4),
          ["<C-Space>"] = cmp.mapping.complete(),
          ["<C-e>"] = cmp.mapping.abort(),
          ["<CR>"] = cmp.mapping.confirm({ select = true }),
        }),
        sources = cmp.config.sources({
          { name = "nvim_lsp" },
          { name = "luasnip" },
        }, {
          { name = "buffer" },
        }),
      })
    end,
  },
}
