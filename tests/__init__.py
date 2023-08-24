from os import getcwd, name
from sys import path

if name == "nt":
    from pathlib import WindowsPath

    p = WindowsPath(getcwd()) / "src"
else:
    from pathlib import PosixPath

    p = PosixPath(getcwd()) / "src"

path.append(str(p))
