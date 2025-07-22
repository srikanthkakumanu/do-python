# Python

This repository demonstrates the features of Python language and its capabilities.

## Installation

Python can be installed in different ways. 

 - Install using apt package manager in Linux.
 - Install Anaconda or Miniconda.

## Anaconda Installation

Important Links: https://www.youtube.com/watch?v=hEBQQU7wKEE&t=32s

1. Install it using

```bash 
bash ~/Downloads/Anaconda3-2025.06-0-Linux-x86_64.sh
```

2. Once Anaconda distribution is downloaded and installed, follow the instructions below.

```bash
~/anaconda3/bin/conda init
exec $SHELL # This commands restarts the shell
```

3. It activates conda shell by default and we need to deactivate conda shell and activate it when required.

```bash
conda config --set auto_activate_base false # To Deactivate base
exec $SHELL # To restart Shell
conda activate base # To activate base again
```
4. Update Conda package manager: ```bash conda update --all```
5. To List Conda installed packages: ```bash conda list | grep matplotlib```
6. To Install Conda packages: ```bash conda search vega_datasets --channel conda-forge``` and ```bash conda install -c conda-forge vega_datasets=0.9.0```
7. To view Anaconda Navigator UI: ```bash anaconda-navigator```


