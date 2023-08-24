# funcclasses

[![PyPI - Version](https://img.shields.io/pypi/v/funcclasses.svg)](https://pypi.org/project/funcclasses)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/funcclasses.svg)](https://pypi.org/project/funcclasses)
[![Code Coverage](https://img.shields.io/codecov/c/github/joshua-auchincloss/spic?style=flat-square)](https://app.codecov.io/github/joshua-auchincloss/tableclasses)

---

**Table of Contents**

- [Installation](#installation)
- [License](#license)
- [Usage](#usage)

## Summary

Class based functional methods

## Installation

```console
pip install funcclasses
```

## Usage

### `partial`

```py
from typing import Callable, SupportsInt, SupportsComplex, SupportsFloat
from beartype import beartype
from funcclasses.partial import partial

Numberlike = SupportsFloat | SupportsComplex | SupportsInt

def my_list_mut(
        func: Callable[[Numberlike, Numberlike], Numberlike],
        a: Numberlike,
        b: Numberlike,
    ):
    return func(a,b)

@beartype
def add(a:Numberlike, b:Numberlike) -> Numberlike:
    return a + b

sum_generic = partial(my_list_mut, add)

if __name__ == "__main__":
    sum_generic(a=21,b=21) # -> 42

```

## License

`funcclasses` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
