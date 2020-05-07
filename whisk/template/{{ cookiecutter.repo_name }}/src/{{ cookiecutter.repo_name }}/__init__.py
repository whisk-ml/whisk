from os.path import dirname, realpath
from pathlib import Path

module_dir = Path(realpath(__file__))
artifacts_dir = module_dir / "artifacts"
data_dir = module_dir.parents[2] / "data"
