from setuptools import setup, find_packages
import pathlib

import pypackage

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="roksikonja_template",  # pip install <name>
    version=pypackage.__version__,
    description="A template Python project with setup, structure, testing and documentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/roksikonja/roksikonja-template",
    author="Rok Šikonja",
    author_email="sikonjarok@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="template, setuptools, development, testing",
    package_dir={"": "src"},  # import <package_name>
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=["numpy"],
    project_urls={
        "Bug Reports": "https://github.com/roksikonja/pyproject/issues",
        "Source": "https://github.com/roksikonja/pyproject/",
    },
)
