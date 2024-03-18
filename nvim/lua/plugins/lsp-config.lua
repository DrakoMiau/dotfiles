return{
    {
        "williamboman/mason.nvim",
        config = function()
            require("mason").setup()
        end
    },
    {
        "williamboman/mason-lspconfig.nvim",
        config = function()
            require("mason-lspconfig").setup({
                ensure_installed = {"lua_ls", "rust_analyzer", "angularls", "bashls", "clangd", "csharp_ls", "cssls", "cssmodules_ls", "unocss", "elixirls", "erlangls", "golangci_lint_ls", "gopls", "graphql", "html", "htmx", "hls", "jsonls", "biome", "jdtls", "java_language_server", "quick_lint_js", "tsserver", "vtsls", "julials", "kotlin_language_server", "ltex", "texlab", "marksman", "prosemd_lsp", "matlab_ls", "perlnavigator", "intelephense", "jedi_language_server", "pyre", "pylsp", "ruby_ls", "solargraph", "sorbet", "sqls", "sqlls", "taplo", "tailwindcss", "volar", "lemminx", "yamlls", "zls"}
            })
        end
    },
    {
        "neovim/nvim-lspconfig",
        config = function()
            local lspconfig = require("lspconfig")
            lspconfig.lua_ls.setup({})
            lspconfig.tsserver.setup({})
            lspconfig.ruby_ls.setup({})
            lspconfig.solargraph.setup({})
            lspconfig.sorbet.setup({})
            lspconfig.sqls.setup({})
            lspconfig.sqlls.setup({})
            lspconfig.taplo.setup({})
            lspconfig.tailwindcss.setup({})
            lspconfig.volar.setup({})
            lspconfig.lemminx.setup({})
            lspconfig.yamlls.setup({})
            lspconfig.zls.setup({})
            lspconfig.rust_analyzer.setup({})
            lspconfig.angularls.setup({})
            lspconfig.bashls.setup({})
            lspconfig.clangd.setup({})
            lspconfig.csharp_ls.setup({})
            lspconfig.cssls.setup({})
            lspconfig.cssmodules_ls.setup({})
            lspconfig.unocss.setup({})
            lspconfig.elixirls.setup({})
            lspconfig.erlangls.setup({})
            lspconfig.golangci_lint_ls.setup({})
            lspconfig.gopls.setup({})
            lspconfig.graphql.setup({})
            lspconfig.html.setup({})
            lspconfig.htmx.setup({})
            lspconfig.hls.setup({})
            lspconfig.jsonls.setup({})
            lspconfig.biome.setup({})
            lspconfig.jdtls.setup({})
            lspconfig.java_language_server.setup({})
            lspconfig.quick_lint_js.setup({})
            lspconfig.vtsls.setup({})
            lspconfig.julials.setup({})
            lspconfig.kotlin_language_server.setup({})
            lspconfig.ltex.setup({})
            lspconfig.texlab.setup({})
            lspconfig.marksman.setup({})
            lspconfig.prosemd_lsp.setup({})
            lspconfig.matlab_ls.setup({})
            lspconfig.perlnavigator.setup({})
            lspconfig.intelephense.setup({})
            lspconfig.jedi_language_server.setup({})
            lspconfig.pyre.setup({})
            lspconfig.pylsp.setup({})
            vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
            vim.keymap.set('n', '<leader>gd', vim.lsp.buf.definition, {})
            vim.keymap.set({ 'n' }, '<leader>ca', vim.lsp.buf.code_action, {})
        end
    }
}
