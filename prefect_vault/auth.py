"""HashiCorp Vault authentication blocks."""


from abc import abstractmethod

import hvac
from prefect.blocks.core import Block
from pydantic import SecretStr


class VaultAuth(Block):
    """Base class for HashiCorp Vault authentication methods.

    See https://www.vaultproject.io/docs/auth.
    """

    _logo_url = "https://raw.githubusercontent.com/hashicorp/vault/main/ui/public/vault-logo.svg"  # noqa

    vault_url: str

    @abstractmethod
    def vault_client(self) -> hvac.Client:
        """Returns Vault client."""


class VaultToken(VaultAuth):
    """HashiCorp Vault token.

    See https://www.vaultproject.io/docs/auth/token.
    """

    _block_type_name = "HashiCorp Vault Token"

    token: SecretStr

    def vault_client(self) -> hvac.Client:
        """Returns Vault client."""
        return hvac.Client(url=self.vault_url, token=self.token.get_secret_value())


class VaultAppRole(VaultAuth):
    """HashiCorp Vault token.

    See https://www.vaultproject.io/docs/auth/approle.
    """

    _block_type_name = "HashiCorp Vault AppRole"

    role_id: str
    secret_id: SecretStr
    mount_point: str = "approle"

    def vault_client(self) -> hvac.Client:
        """Returns Vault client."""
        client = hvac.Client(url=self.vault_url)
        client.auth.approle.login(
            role_id=self.role_id,
            secret_id=self.secret_id.get_secret_value(),
            mount_point=self.mount_point,
        )
        return client
