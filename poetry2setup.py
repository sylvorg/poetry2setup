#!/usr/bin/env python3

from pathlib import Path

from poetry.core.factory import Factory
from poetry.core.masonry.builders.sdist import SdistBuilder



def build_setup_py(path = "."):
    return SdistBuilder(Factory().create_poetry(Path(path).resolve())).build_setup()


def main():
    print(build_setup_py().decode("utf8"))


if __name__ == "__main__":
    main()
