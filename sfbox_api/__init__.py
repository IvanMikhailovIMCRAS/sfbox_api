import os

from .composition import Composition
from .run import run

target = f"{os.path.dirname(os.path.realpath(__file__))}/data/sfbox"
os.system(f"chmod +x {target}")


__all__ = ["Composition", "run"]
