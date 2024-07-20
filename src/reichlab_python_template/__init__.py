import importlib.util
from pathlib import Path

__version__ = "0.0.1"

MODULE_PATH = Path(importlib.util.find_spec("reichlab_python_template").origin).parent
CONFIG_PATH = MODULE_PATH / "conf" / "config.toml"
