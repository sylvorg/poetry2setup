#!/usr/bin/env python3

from pathlib import Path

from poetry.core.factory import Factory
from poetry.core.masonry.builders.sdist import SdistBuilder

from os.path import expandvars


def erPath(path):
    if path:
        return (path if isinstance(path, Path) else Path(expandvars(path))).expanduser().resolve(strict = True)
    else:
        return path


def build_setup_py(path = "."):
    return SdistBuilder(Factory().create_poetry(erPath(path))).build_setup().decode("utf8")


def main():
    print(build_setup_py())


if __name__ == "__main__":
    main()
