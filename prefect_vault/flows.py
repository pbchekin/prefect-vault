"""This is an example flows module"""
from prefect import flow

from prefect_vault.tasks import (
    goodbye_prefect_vault,
    hello_prefect_vault,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_vault)
    print(goodbye_prefect_vault)
    return "Done"
