# uv

uv is a package manager for Python that replaces:

- pip (package installer)
- venv (virtual environment manager)
- pip-tools (dependency management)
- pyenv (Python version management)

Written in Rust, it’s blazingly fast and just works.

## Common commands

```bash

# Create new project
uv init project-name

# Add packages
uv add package-name

# Remove packages
uv remove package-name

# Install all dependencies
uv sync

# Update packages
uv add --upgrade package-name

# Show installed packages
uv pip list

# Run Python scripts
uv run python script.py

```
## Working with existing projects

Got a project with `requirements.txt`? No problem:

```bash
# Convert requirements.txt to pyproject.toml
uv add -r requirements.txt

# Or just install from requirements.txt
uv pip install -r requirements.txt
```

### Using uv without deleting anything in the project


To use uv without deleting anything in your Python project, you can follow these steps:

1. Ensure your project is activated with `uv venv` or `uv activate` to use the current virtual environment.
2. Use `uv pip install -r requirements.txt` to install all packages listed in your `requirements.txt` file.
3. If you have a `pyproject.toml` file, you can use `uv sync` to update the `pyproject.toml` to match the installed packages.
4. If you need to remove a package, use `uv remove <package_name>` to uninstall it from your environment.
5. To upgrade a package, run `uv lock` with the `--upgrade-package` flag to update the specified package to the latest compatible version.
6. This way, you can manage your Python project's dependencies without affecting the existing virtual environment or `requirements.txt` file.

## Tips and tricks

1. Global tools: Install tools globally with uv

```bash
# Install tools globally
uv tool install black
uv tool install mypy
```
2. Python versions: uv can manage Python too.

```bash
uv python install 3.12
uv python install 3.11
```

3. Scripts: Add custom commands

```bash
[project.scripts]
start = "ai_assistant.main:run"
test = "pytest tests/"
```

4. Environment variables: Add environment variables to your project using uv

```toml
[tool.uv]
env = [
    "VARIABLE_NAME=VALUE",
]
```