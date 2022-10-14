# prefect-vault

## Welcome!

Prefect blocks for HashiCorp Vault.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-vault` with `pip`:

```bash
pip install prefect-vault
```

### Create VaultSecret block with token authentication

```python
from prefect_vault import VaultSecret, VaultToken

vault_secret = VaultSecret(
    vault_auth=VaultToken(
        vault_url='http://myvault:8200',
        token='my_secret_token',
    ),
)

await vault_secret.save('my-vault-secret')
```

### Create VaultSecret block with approle authentication

```python
from prefect_vault import VaultAppRole, VaultSecret 

vault_secret = VaultSecret(
    vault_auth=VaultAppRole(
        vault_url='http://myvault:8200',
        role_id='my_role_id',
        secret_id='my_secret_id',
    ),
)

await vault_secret.save('my-vault-secret')
```

### Use VaultSecret in Prefect flow

```python
from prefect import flow
from prefect_vault import VaultSecret


@flow
async def use_vault_secret():
    vault_secret = await VaultSecret.load('my-vault-secret')
    secret_value = vault_secret.get_secret('path/to/my/secret')['secret_key']
```

## Resources

If you encounter any bugs while using `prefect-vault`, feel free to open an issue in the [prefect-vault](https://github.com/pbchekin/prefect-vault) repository.

If you have any questions or issues while using `prefect-vault`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-vault` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/pbchekin/prefect-vault.git

cd prefect-vault/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
