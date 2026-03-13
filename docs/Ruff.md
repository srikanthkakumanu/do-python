## Using Ruff for Python Code Formatting

Ruff is a fast Python code formatter and linter designed as a drop-in replacement for Black. It ensures consistent formatting while focusing on performance. Here's how to use Ruff to format Python code:

1. **Format Code with Ruff**: Ruff provides the ruff format command to format Python files or directories.

- Format all files in the current directory: `ruff format`

- Format a specific file: `ruff format path/to/file.py`

Check formatting without modifying files: `ruff format --check path/to/file.py`

2. **Configure Formatting Options**: You can customize Ruff's behavior by adding configurations in `pyproject.toml` or `ruff.toml`. For example:

```toml
[tool.ruff.format]
line-length = 88
quote-style = "single"
indent-style = "space"
docstring-code-format = true
```

This configures line length, quote style, indentation, and docstring formatting.

3. **Suppress Formatting for Specific Code Blocks** Use comments like `# fmt: off` and `# fmt: on` to disable formatting for specific sections:

```toml
# fmt: off
unformatted_code = [ 'example', 'list' ]
# fmt: on
```
4. Validate Changes Run Ruff with the `--diff` flag to preview changes before applying them:

```
ruff format --diff path/to/file.py
```
Tips:

Ruff integrates seamlessly with linters and supports pre-commit hooks for automated formatting.

It adheres closely to Black's style but offers additional configuration options.