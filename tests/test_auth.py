from prefect_vault.auth import VaultToken

# def test_vault_app_role():
#     vault_block = VaultAppRole(
#         vault_url='http://127.0.0.1:8200', token='unsafe-root-token'
#     )
#     assert vault_block.vault_client().is_authenticated()


def test_vault_token():
    vault_block = VaultToken(
        vault_url="http://127.0.0.1:8200", token="unsafe-root-token"
    )
    assert vault_block.vault_client().is_authenticated()
