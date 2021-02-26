# Python Project Structure

This is a template project for Python. 
In the ```README.md``` a quick summary with workflow is described.
For more refer to the documentation.

## Project Structure


        mkdir pyproject
        cd pyproject

        # venv setup
        python -m venv venv
        .\venv\Scripts\activate
        python -m pip install --upgrade pip setuptools wheel pytest
        python -m pip install --upgrade pip
        
        pip install --upgrade setuptools wheel pytest
        deactivate

        cd C:\roksikonja\pyproject

        # vcs
        git init
        .gitignore

        # install from source
        python -m pip install --editable .
        pip install --editable .

        # run package as script
        # as defined in pypackage/__main__.py
        python -m pypackage

        
        cd /mnt/c/roksikonja/pyproject
        tree -I "venv|bin|dist|build|*.py[cod]|*.egg-info|__pycache__"

        # check installation
        pip list
        pyproject 0.0.1 c:\roksikonja\pyproject\src

        # test
        python -m pytest tests/
        # without cache
        python -m pytest -p no:cacheprovider tests/

        # build
        python -m pip install --upgrade build
        C:\roksikonja\pyproject\venv\Scripts\python.exe -m build
        python -m build

        python setup.py sdist bdist_wheel
        twine check dist/*

        # deploy to testpypi using token in .pypirc
        python -m pip install --upgrade twine
        
        # check builds
        twine check dist/*
        twine upload --repository testpypi dist/*

        twine upload dist/*
        python -m twine upload --repository testpypi dist/*

        # install
        python -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyproject
        pip install -i https://test.pypi.org/simple/ roksikonja-template

        pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple roksikonja-template


* Files:
    * MANIFEST.in: Specify what to include/exclude in the source distribution, not affecting binary distribution (wheel)
        * [Guide](https://packaging.python.org/guides/using-manifest-in/#using-manifest-in)
        * Automatically added: py modules and packages, scripts, data_files/package_data, licence, test/test*.py, setup.*, README.*, pyproject.toml, MANIFEST.in

### Build

        # source build
        python setup.py sdist

        # wheel
        python setup.py bdist_wheel

        # builds in dist/


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
