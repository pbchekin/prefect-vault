import os

from prefect_vault.auth import VaultAppRole, VaultToken


def test_vault_app_role():
    vault_block = VaultAppRole(
        vault_url=os.environ["PREFECT_VAULT_ADDR"],
        role_id=os.environ["PREFECT_VAULT_ROLE_ID"],
        secret_id=os.environ["PREFECT_VAULT_SECRET_ID"],
    )
    assert vault_block.vault_client().is_authenticated()


def test_vault_token():
    vault_block = VaultToken(
        vault_url=os.environ["PREFECT_VAULT_ADDR"],
        token=os.environ["PREFECT_VAULT_TOKEN"],
    )
    assert vault_block.vault_client().is_authenticated()
