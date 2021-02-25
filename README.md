# Python Project Structure


## References

Adapted from ```https://github.com/pypa/sampleproject```.
* [Publishing well-formed Python packages](https://www.youtube.com/watch?v=_b8D4v7YIME)
* [Shipping your first Python package and automating future publishing](https://www.youtube.com/watch?v=P3dY3uDmnkU)
* [Inside the Cheeseshop: How Python Packaging Works](https://www.youtube.com/watch?v=AQsZsgJ30AE)
* [Python Packaging Guide](https://packaging.python.org)
* [PyPI Publishing](https://realpython.com/pypi-publish-python-package/)

## Project Structure
        .
        ├── LICENSE.txt
        ├── MANIFEST.in
        ├── README.md
        ├── docs
        ├── pyproject.toml
        ├── setup.cfg
        ├── setup.py
        ├── src
        │   └── pypackage
        │       ├── __about__.py
        │       ├── __init__.py
        │       └── base.py
        ├── structure.txt
        └── tests
        └── test_template.py


        mkdir pyproject
        cd pyproject

        # venv setup
        python -m venv venv
        .\venv\Scripts\activate
        python -m pip install --upgrade pip setuptools wheel pytest
        python -m pip install --upgrade pip
        
        pip install --upgrade setuptools wheel pytest
        deactivate

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



        # documentation
        python -m pip install --ugrade sphinx

        mkdir docs
        cd docs
        sphinx-quickstart

* Files:
    * MANIFEST.in: Specify what to include/exclude in the source distribution, not affecting binary distribution (wheel)
        * [Guide](https://packaging.python.org/guides/using-manifest-in/#using-manifest-in)
        * Automatically added: py modules and packages, scripts, data_files/package_data, licence, test/test*.py, setup.*, README.*, pyproject.toml, MANIFEST.in

# Build

        # source build
        python setup.py sdist

        # wheel
        python setup.py bdist_wheel

        # builds in dist/