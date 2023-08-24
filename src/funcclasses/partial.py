from inspect import Parameter, signature
from typing import Callable, Generic

from funcclasses.types import Params, Return


class partial(Generic[Params, Return]):  # noqa: N801
    wrapped: Callable[Params, Return]

    provided: dict
    nparams: int
    parameters: list[Parameter]

    def __init__(self, func: Callable[Params, Return], *args: Params.args, **kwargs: Params.kwargs):
        self.parameters = list(signature(func).parameters.values())
        self.nparams = len(self.parameters)
        self.provided = self.convert_args(*args, **kwargs)

        def wrapped(*args: Params.args, **kwargs: Params.kwargs):
            kwargs = self.overload(args, kwargs)
            return func(**kwargs)

        self.wrapped = wrapped

    def __call__(self, *args: Params.args, **kwargs: Params.kwargs) -> Return:
        return self.wrapped(*args, **kwargs)

    def overload(self, args: list, kwargs: dict):
        kwargs = self.convert_args(*args, **kwargs)
        return {**self.provided, **kwargs}

    def convert_args(self, *args: Params.args, **kwargs: Params.kwargs) -> dict:
        for i, arg in enumerate(args):
            if i == self.nparams:
                msg = "number of args %d exceeds cap" % len(args)
                raise IndexError(msg)
            param: Parameter = self.parameters[i]
            if kwargs.get(param.name):
                msg = f"arg {i} overwrites keyword argument {param.name}. provided keyword arguments must be respected."
                raise KeyError(msg)
            kwargs[param.name] = arg
        return kwargs
