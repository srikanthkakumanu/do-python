# Python Installation Guide

This guide covers different methods for installing Python and package managers on various operating systems.

## Table of Contents
1. [Basic Python Installation](#basic-python-installation)
2. [Anaconda Installation](#anaconda-installation)
3. [Miniconda Installation](#miniconda-installation)
4. [Shell Aliases](#shell-aliases)

## Basic Python Installation

Python can be installed using package managers:

### Linux
```bash
sudo apt update
sudo apt install python3
```

### macOS
```bash
brew install python
```

## Anaconda Installation

Anaconda is a free and open-source distribution of Python and R for scientific computing.

### Linux Installation

1. **Download Anaconda**
   - Download the Linux installer from the official Anaconda website
   - Reference: [Installation Tutorial](https://www.youtube.com/watch?v=hEBQQU7wKEE&t=32s)

2. **Install Anaconda**
   ```bash
   bash ~/Downloads/Anaconda3-2025.06-0-Linux-x86_64.sh
   ```

3. **Initialize Conda**
   ```bash
   ~/anaconda3/bin/conda init
   exec $SHELL  # Restart the shell
   ```

4. **Configure Auto-activation**
   ```bash
   conda config --set auto_activate_base false  # Deactivate base by default
   exec $SHELL  # Restart shell
   conda activate base  # Activate when needed
   ```

5. **Update Conda**
   ```bash
   conda update --all
   ```

6. **Package Management**
   ```bash
   # List installed packages
   conda list | grep matplotlib
   
   # Search for packages
   conda search vega_datasets --channel conda-forge
   
   # Install packages
   conda install -c conda-forge vega_datasets=0.9.0
   ```

7. **Launch Anaconda Navigator**
   ```bash
   anaconda-navigator
   ```

8. **Configure IDE**
   - To use Anaconda with PyCharm, change the Python interpreter to point to the Anaconda3 installation in project settings.

## Miniconda Installation

Miniconda is a minimal installer for conda.

### macOS
```bash
brew install --cask miniconda
```

## Shell Aliases

Create convenient aliases for Python commands.

### macOS

1. **Open shell configuration file**
   - For bash: `~/.bash_profile`
   - For zsh: `~/.zshrc`

2. **Add alias**
   ```bash
   alias P='python3'
   ```

3. **Apply changes**
   ```bash
   # For bash
   source ~/.bash_profile
   
   # For zsh
   source ~/.zshrc
   ```



