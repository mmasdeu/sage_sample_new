# Sample package

This package does not do much, but it illustrates how to write a proper python package for Sage.

![doc](https://github.com/mmasdeu/sage_sample_new/actions/workflows/doc.yml/badge.svg)

![test](https://github.com/mmasdeu/sage_sample_new/actions/workflows/test.yml/badge.svg)

![lint](https://github.com/mmasdeu/sage_sample_new/actions/workflows/lint.yml/badge.svg)

## Installation

### Set up in a conda environment

```
mamba env update -f environment.yml
pip install --no-dependencies git+https://github.com/mmasdeu/sage_sample_new
```

## Usage

From `sage`, you can do:
```
from darmonpoints.darmonpoint import *
darmon_point() # Should output the answer to the ultimate question
```

See https://mmasdeu.github.io/sage_sample_new for more examples.
