# The minipy package

Small Python packages with some essentials to start new projects.

This is a small demo packages having just a few essential files to start a new project as a Python package easily.

The repository contains the following essential files:

* `README.md` - the file you are reading
* `setup.py` -  the setup file for the package install
* `LICENSE` - the license file, here a MIT license
* `minipy/add.py` - the example add function with docstring documentation embedded
* `minipy/\_\_main\_\_.py` - the file containing an example application runnable with `python -m minipy`
* `minipy/\_\_init\_\_.py - the initialization coce - this file makes the module a package

## Cloning

To create new projects you can just fetch the package to your file system using your download manager pointing to:

![https://github.com/mittelmark/minipy/archive/refs/heads/main.zip](https://github.com/mittelmark/minipy/archive/refs/heads/main.zip) or using Git.

Fetching the zip might be done like this:

```
wget https://github.com/mittelmark/minipy/archive/refs/heads/main.zip
```
cloning via git:

```
git clone https://github.com/mittelmark/minipy.git
```

If you clone, just remove the .git folder afterwards and then rename the new folder
## Installation

To directly install the package try this:

```
pip3 install git+https://github.com/mittelmark/minipy.git --user
# after successfull install try this
python3 -c "import minipy;print(minipy.add(2,3))"
```

This is not useful if you like to use this as a starting package but it shows you how users of your package could directly install them from Github or other git repositories.

You can as well run the sample program in the file `\_\_main\_\_.py` from any folder like this:

```
python3 -m minipy
```

The documentation should be readable like this:

```
pydoc3 minipy
# and for the add function
pydoc3 minipy.add
```
