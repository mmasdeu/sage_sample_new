---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.15.2
kernelspec:
  display_name: SageMath 10.2
  language: sage
  name: sagemath
---

# Example notebook

## How to use darmonpoints

```{code-cell}
---
jupyter:
  outputs_hidden: false
---
from darmonpoints.darmonpoint import *
darmon_point() # Should output the answer to the ultimate question
```

## Here is a stupid plot

Maybe you enjoy seeing a plot of $y=\sin(x)$. In this case, here you go:


```{code-cell}
---
jupyter:
  outputs_hidden: false
---
plot(sin,0,2*pi)
```
