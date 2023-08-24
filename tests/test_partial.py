from funcclasses.partial import partial


def test_noargs_partial():
    def noargs() -> int:
        return 1

    p = partial(noargs)

    assert p() == 1


def test_arg1_partial():
    def arg1(a: int) -> int:
        return a

    p = partial(arg1, a=1)
    assert p() == 1
    assert p(a=2) == 2
    p = partial(arg1, 1)
    assert p() == 1
    assert p(a=2) == 2
    p = partial(arg1)
    assert p(a=1) == 1


def test_arg2_partial():
    def arg2(a: int, b: int) -> int:
        return a + b

    p = partial(arg2, a=1)

    assert p(b=2) == 3
    assert p(2, b=2) == 4
    assert p(a=2, b=2) == 4
    assert p(2, 2) == 4

    p = partial(arg2, 1, 2)
    assert p() == 3
    assert p(a=2) == 4
    assert p(2) == 4

    p = partial(arg2, 1, b=2)
    assert p() == 3
    assert p(a=2) == 4
    assert p(2) == 4

    p = partial(arg2)
    assert p(a=1, b=2) == 3


def uncaught():
    msg = "not caught"
    raise RuntimeError(msg)


def test_invalid():
    def args(a: int, b: int):
        return a + b

    try:
        p = partial(args, 1, 2, 3)
        uncaught()
    except RuntimeError as e:
        raise e
    except IndexError:
        pass

    try:
        p = partial(args, 1, 2, a=1)
        uncaught()
    except RuntimeError as e:
        raise e
    except KeyError:
        pass

    p = partial(args)
    try:
        p(1, 2, a=1)
        uncaught()
    except RuntimeError as e:
        raise e
    except KeyError:
        pass
