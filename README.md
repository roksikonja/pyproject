# Template Python Project

This is a template project for Python. 
In the ```README.md``` a quick summary with workflow is described.
For more refer to the documentation in ```docs/```.
Commands are given to be executed in Powershell.

Some commands are added just to have a quick reference if forgotten, 
thus can be considered as a cheat sheet. 


## Project Structure

    # get tree structure in WSL2
    cd /mnt/c/roksikonja/pyproject
    tree -I "venv|bin|dist|build|*.py[cod]|*.egg-info|__pycache__|.pytest_cache"

    .
    ├── LICENSE.txt
    ├── MANIFEST.in
    ├── README.md
    ├── docs
    │   ├── Makefile
    │   ├── make.bat
    │   └── source
    │       ├── _static
    │       ├── _templates
    │       ├── conf.py
    │       ├── index.rst
    │       └── *.rst
    ├── pyproject.toml  # build configuration
    ├── requirements.txt
    ├── setup.cfg  # static configuration
    ├── setup.py  # dynamic configuration
    ├── src
    │   └── pypackage
    │       ├── __about__.py
    │       ├── __init__.py
    │       ├── __main__.py  # entry point for python -m pypackage
    │       ├── base.py
    │       ├── google_style.py
    │       └── module.py
    └── tests
        └── test_template.py


## Python

    # create project directory
    mkdir pyproject
    cd pyproject

    # venv setup
    python -m venv venv

    # activate venv
    .\venv\Scripts\activate
    deactivate

    # update or install build and packaging tools
    python -m pip install --upgrade pip
    pip install --upgrade setuptools wheel
            
    # install from source for development
    pip install --editable .

    # install from pypi for usage as library
    pip install roksikonja-template  # specified in setup.py/name

    # run package as script
    python -m pypackage

    # freeze dependecies of the whole Python environment
    pip freeze > requirements.txt
    pip install -r requirements.txt
    
    # check installation
    pip list
    pyproject 0.0.1 c:\roksikonja\pyproject\src


### Testing

    # install pytest
    pip install --upgrade pytest

    # run test
    pytests
    pytest tests/
    pytest -p no:cacheprovider tests/ # without cache


### Building

    # install build tools
    pip install --upgrade build

    # build
    python -m build
    python setup.py sdist bdist_wheel

    # builds in dist/


### Publishing

    # install twine publishing tool
    pip install --upgrade twine
    
    # verify builds
    twine check dist/*
    
    # deploy to testpypi using token in ~/.pypirc
    twine upload --repository testpypi dist/*
    twine upload --skip-existing --repository testpypi dist/*
    
    # deploy to pypi using token in ~/.pypirc
    twine upload dist/*
    twine upload --skip-existing dist/*
    
    # install from testpy
    # install dependencies manually
    pip install -i https://test.pypi.org/simple/ roksikonja-template --no-deps
    
    # install dependencies from pypy
    pip install \
        --index-url https://test.pypi.org/simple/ \
        --extra-index-url https://pypi.org/simple roksikonja-template


## Documentation

Documentation using Sphinx.

### Installation

    mkdir docs
    cd docs

    # install Sphinx
    pip install --upgrade sphinx

    # markdown support
    pip install --upgrade recommonmark

    # generate documentation
    sphinx-quickstart
    
    # update conf.py in docs/source


### Usage            

    # add page in Markdown/RestructuredText
    page.*
  
    # add to toc
    Page Title <page.*>
  
    # add in *.rst file to include docstrings from code
    .. automodule:: <module_name>
    .. autoclass:: <class_name>
  
    # generate html
    make html  # .\make.bat html  # powershell
    
    # view documentation
    cd .\docs\build\html
    start firefox index.html


### Documenting Code

    # add package directory to sys.path in conf.py

    # in each file add a docstring on the first line
    # of a file, module, function, class
    """Docstring starts immediately after three double quotes.
    """

## Type Checking

    # install mypy
    pip install mypy
    
    # check types
    mypy src -v  


## Version Control

    # initialize git project with main branch
    git init -b main
    git remote add origin https://github.com/roksikonja/pyproject.git

    # workflow
    git add <file_name>
    git commit -m "message"
    git push origin main

    # ignore files
    .gitignore


## Conda Package Manager

Python packaging for scientific computing with ```conda```.
* [Cheat Sheet](https://conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
  
        # ensure conda is in path
        conda --version
        conda info
        conda update    

        # create conda (virtual) environment using python 3.x
        conda create --name <venv_name> python=3.x
        conda activate <venv_name>
        conda deactivate

        # list conda environments
        conda env list
        conda remove env -n <venv_name>
        
        # list installed packages
        cond list

        # install pip in conda environment
        conda install pip
        pip install -e .


# TODO

* https://github.com/ubernostrum/webcolors
* tox
* docs
* formatting + flake8
* https://www.b-list.org/weblog/2020/jan/05/packaging/
* test coverage
* https://www.b-list.org/weblog/2020/feb/03/how-im-testing-2020/

# Code Quality

Configurations added to ```setup.cfg``` and ```pyproject.toml```.

    pip install pydocstyle flake8 mypy pylint isort coverage

    pytest tests
    mypy
    black .
    flake8
    pylint src/ scripts/
    isort .
    pydocstyle src/ tests/

    # docs
    cd docs
    .\make.bat html -b spelling
