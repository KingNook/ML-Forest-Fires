"""
Boilerplate for other test documents
"""

"""
BOILERPLATE
"""

import pytest
from pathlib import Path

BASE_PATH = Path().parent.parent
DATA_PATH = BASE_PATH / "data"

FIRE_DATA = DATA_PATH / "_FIRE"
ZARR_DATA = DATA_PATH / "_ZARR_READY"

TEST_MAIN = DATA_PATH / "alaska_main"
TEST_PRIOR = DATA_PATH / "alaska_prior"

"""
TESTS
"""