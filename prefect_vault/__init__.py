from . import _version
from .auth import VaultAppRole, VaultToken
from .secret import VaultSecret


__all__ = ["VaultAppRole", "VaultSecret", "VaultToken"]


__version__ = _version.get_versions()["version"]
