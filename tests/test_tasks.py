from prefect import flow

from prefect_vault.tasks import (
    goodbye_prefect_vault,
    hello_prefect_vault,
)


def test_hello_prefect_vault():
    @flow
    def test_flow():
        return hello_prefect_vault()

    result = test_flow()
    assert result == "Hello, prefect-vault!"


def goodbye_hello_prefect_vault():
    @flow
    def test_flow():
        return goodbye_prefect_vault()

    result = test_flow()
    assert result == "Goodbye, prefect-vault!"
