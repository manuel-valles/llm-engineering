[UV](https://docs.astral.sh/uv/) is a tool for managing Python environments and packages. For Windows users:

1. Install UV: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Add the command line `export PATH="$HOME/.local/bin:$PATH"` to `~/.bash_profile`
3. Check for latest updates: `uv self update`

Once you have it installed, you just need a `toml` file with all the Python dependencies and a `.python-version` for compatibilities. Then just run: `uv sync`.