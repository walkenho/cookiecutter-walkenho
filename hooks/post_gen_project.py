"""Python that runs after the project is generated.

Read more: https://cookiecutter.readthedocs.io/en/1.7.3/advanced/hooks.html
"""

from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path(".")


if __name__ == "__main__":
    # Rename templated files
    os.rename(PROJECT_DIRECTORY / "pyproject.template.toml", PROJECT_DIRECTORY / "pyproject.toml")
