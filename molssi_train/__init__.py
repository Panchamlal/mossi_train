"""
molssi_train
This is the project for molssi training.
"""

# Add imports here
from .molssi_math import canvas, mean
from .string_util import title_case

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
