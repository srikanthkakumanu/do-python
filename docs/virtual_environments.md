# Virtual Environments

Virtual environment can be installed using this command in a desired directory: `python3 -m venv .venv`

A created virtual environment can be activated via: `source .venv/bin/activate` and it can be de-activated via `deactivate`.

We can freeze the environment and creating requirements.txt → `pip3 freeze > requirements.txt`

To use `requirements.txt`, we need to use this command after venv is installed and activated: `pip3 install -r requirements.txt`

Note: Make sure you select right virtual environment based python interpreter. Homebrew (system) environment is different and .venv environment is different. Both use different pip3 environments to avoid conflicts or collision of packages.

Alternatively, **uv** is a blazingly fast package manager for Python that replaces `pip`, `venv`, and more.

Common commands:

```bash
# Create new project
uv init project-name

# Add packages
uv add package-name

# Install all dependencies
uv sync

# Run Python scripts
uv run python script.py
```

For more details, see [uv Guide](docs/uv.md).