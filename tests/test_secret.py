import os

from prefect_vault.auth import VaultToken
from prefect_vault.secret import VaultSecret


def test_put_get_secret():
    vault_secret = VaultSecret(
        vault_auth=VaultToken(
            vault_url=os.environ["PREFECT_VAULT_ADDR"],
            token=os.environ["PREFECT_VAULT_TOKEN"],
        ),
    )
    vault_secret.put_secret("test", {"key": "value"})
    secret = vault_secret.get_secret("test")
    assert secret == {"key": "value"}


async def test_save_load():
    vault_secret = VaultSecret(
        vault_auth=VaultToken(
            vault_url=os.environ["PREFECT_VAULT_ADDR"],
            token=os.environ["PREFECT_VAULT_TOKEN"],
        ),
    )
    vault_secret.put_secret("test", {"key": "value"})
    await vault_secret.save("vault-secret", overwrite=True)

    vault_secret = await VaultSecret.load("vault-secret")
    secret = vault_secret.get_secret("test")
    assert secret == {"key": "value"}
