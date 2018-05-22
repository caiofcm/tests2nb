[![Build Status](https://travis-ci.org/caiofcm/tests2nb.svg?branch=master)](https://travis-ci.org/caiofcm/tests2nb)

# TESTS2NB: Python Tests To Notebook Converter

This is a small utility for turning python test scripts into Jupyter notebooks.

## Why?

Jupyter notebook are interactive and easier to read, thus it is a good resource
to share and explore ideas. Tests can serve as living documentation for a code funcionality.
I wanted a tool to aggregate the benefits of writing tests as regular pytest scripts but 
being able to get a jupyter notebook for easer reading and exploring conditions.  

## Install

Install using `pip`:

```bash
pip install git+https://github.com/caiofcm/tests2nb.git
```

Alternatively, you can create a local clone of this repository and install
from it:

```bash
git clone https://github.com/caiofcm/tests2nb.git
pip install -r requirements.txt
```

## Usage


To convert a python test script into a notebook:

```bash
python -m tests2nb ../samples/test_wallet.py out_.ipynb
```

## Samples

See `tests` directory.

## How It Works

- Uses `ast` to convert python tests to a intermediary python test file (thus original formatting is disregarded and comments are removed)
- Uses [py2nb](https://github.com/sklam/py2nb/tree/master/py2nb) to convert the intermediary python file to jupyter notebook

