"""HashiCorp Vault secret block."""


from typing import Any, Dict, Optional

from prefect.blocks.core import Block

from prefect_vault.auth import VaultAuth


class VaultSecret(Block):
    """HashiCorp secret."""

    vault_auth: VaultAuth

    def get_secret(self, path: str, mount_point="secret") -> Optional[Dict[str, Any]]:
        """Returns Vault secret."""
        vault_client = self.vault_auth.vault_client()
        return (
            vault_client.secrets.kv.v2.read_secret(path=path, mount_point=mount_point)
            .get("data", {})
            .get("data")
        )

    def put_secret(self, path: str, secret: Dict[str, Any], mount_point="secret"):
        """Creates or updates Vault secret."""
        vault_client = self.vault_auth.vault_client()
        vault_client.secrets.kv.v2.create_or_update_secret(
            path=path, secret=secret, mount_point=mount_point
        )
