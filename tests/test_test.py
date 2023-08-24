from typing import Callable, SupportsComplex, SupportsFloat, SupportsInt

from beartype import beartype

from funcclasses.partial import partial

Numberlike = SupportsFloat | SupportsComplex | SupportsInt


def my_list_mut(
    func: Callable[[Numberlike, Numberlike], Numberlike],
    a: Numberlike,
    b: Numberlike,
):
    return func(a, b)


@beartype
def add(a: Numberlike, b: Numberlike) -> Numberlike:
    return a + b


sum_generic = partial(my_list_mut, add)


def test_sum_generic():
    sum_generic = partial(my_list_mut, add)
    assert sum_generic(a=21, b=21) == 42
